import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { CubejsClient } from "@cubejs-client/ngx";
import { Subject } from "rxjs";

@Component({
  selector: 'app-selecao-litigante',
  templateUrl: './selecao-litigante.component.html',
  styleUrls: ['./selecao-litigante.component.scss']
})
export class SelecaoLitiganteComponent implements OnInit {

  @Input() query;
  @Output() eventoLitiganteSelecionado = new EventEmitter();

  constructor(private cubejs: CubejsClient) {}

  private querySubject;

  public litigantes;

  //private jQuery: any;

  commonSetup(resultSet) {

    this.litigantes = resultSet.chartPivot().map(element => ({
        id: element["category"],
        name: element["category"]
    })); 
  }

  onSelectLitigante(litigante) {
    this.eventoLitiganteSelecionado.emit(litigante);
  }

  resultChanged(resultSet) {
    this.commonSetup(resultSet);
  }

  ngOnInit() {
    this.querySubject = new Subject();
    this.resultChanged = this.resultChanged.bind(this);
    this.cubejs
      .watch(this.querySubject)
      .subscribe(this.resultChanged, err => console.log("HTTP Error", err));

    this.querySubject.next(this.query);
  }

  ngAfterViewInit() {
  } 

}