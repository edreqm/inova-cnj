import { Component } from "@angular/core";

@Component({
  selector: "app-root",
  templateUrl: "./app.component.html",
  styleUrls: []
})
export class AppComponent {

  public nomesLitigantesQuery = {
    dimensions: [
      "PerformanceVara.nomeDoLitigante"
    ],
  };

  public performanceLitiganteVaraQuery = {};

  public litiganteSelecionado;

  filtraLitigante(litigante) {
    this.litiganteSelecionado = litigante;
    this.performanceLitiganteVaraQuery = {
      measures: [
        "PerformanceVara.fitness",
        "PerformanceVara.tempo"
      ],
      dimensions: [
        "PerformanceVara.nomeDaVara",
        "PerformanceVara.nomeDoLitigante"
      ],
      filters: [
        {
          "dimension": "PerformanceVara.nomeDoLitigante",
          "operator": "equals",
          "values": [
            litigante
          ]
        }
      ],
      order: {
        "PerformanceVara.fitness": "asc",
        "PerformanceVara.tempo": "asc"
      }
    };
  }

  constructor() {}

  ngOnInit() {}
}