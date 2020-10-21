import { Component, OnInit, Input, KeyValueDiffer, KeyValueDiffers } from "@angular/core";
import { CubejsClient } from "@cubejs-client/ngx";
import { Subject } from "rxjs";
import * as d3 from 'd3';
import * as d3Scales from 'd3-scale'
import { ResultSet } from '@cubejs-client/core';

@Component({
  selector: 'app-heat-map',
  templateUrl: './heat-map.component.html',
  styleUrls: ['./heat-map.component.scss']
})
export class HeatMapComponent implements OnInit {

  @Input() chartType;
  @Input() query;
  @Input() title;

  constructor(private cubejs: CubejsClient, private differs: KeyValueDiffers) {}

  public chartData;
  public chartLabels;

  public d3Data;

  private queryDiffer: KeyValueDiffer<string, any>;

  public ready = false;

  private numberFormatter = x => (Math.round(x * 100) / 100).toFixed(2);

  private svg;
  private margin = 50;
  private width = 750 - (this.margin * 2);
  private height = 500 - (this.margin * 2);

  private xLabel = 'Tempo de duração';
  private yLabel = 'Fitness do processo';


  commonSetup(resultSet) {

    this.d3Data = resultSet.chartPivot().map(element => (
      {
        x: element["PerformanceVara.tempo"],
        y: element["PerformanceVara.fitness"],
        categoria: element["category"]
      })); 
  }

  resultChanged(resultSet) {
    this.createSvg();
    this.commonSetup(resultSet);
    this.drawHeatMap(this.d3Data)
    this.ready = true;
  }

  ngOnInit() {
   this.queryDiffer = this.differs.find(this.query).create();
  }

  ngDoCheck() {
    const changes = this.queryDiffer.diff(this.query);
    if (changes) {
      this.queryChanged();
    }
  }

  queryChanged() {
    this.cubejs.load(this.query).subscribe( 
      resultSet => this.resultChanged(resultSet), 
      err => console.log("HTTP Error", err));
  }


  createSvg() {
    if (this.svg != null) {
      d3.select("svg#grafico").remove();
    }
    this.svg = d3.select("figure#heat_map")
    .append("svg")
    .attr("id", "grafico")
    .attr("width", this.width + (this.margin * 2))
    .attr("height", this.height + (this.margin * 2))
    .append("g")
    .attr("transform", "translate(" + this.margin + "," + this.margin + ")");
  }

  drawHeatMap(data) {

    let minX = Math.min.apply(null, this.d3Data.map(e => (e.x)));
    
    // Diminui um pouco para que o primeiro ponto não fique exatamente sobre o eixo
    minX = minX - 0.05*minX
    let maxX = Math.max.apply(null, this.d3Data.map(e => (e.x)));

    // Aumenta um pouco para que o primeiro ponto não fique exatamente sobre o eixo
    maxX = maxX + 0.05*maxX

    let minY = Math.min.apply(null, this.d3Data.map(e => (e.y)));

    // Diminui um pouco para que o primeiro ponto não fique exatamente sobre o eixo
    minY = minY - 0.05*minY

    let maxY = Math.max.apply(null, this.d3Data.map(e => (e.y)));

    // Aumenta um pouco para que o primeiro ponto não fique exatamente sobre o eixo
    maxY = maxY + 0.05*maxY

    // Add X axis
    var x = d3.scaleLinear()
      .domain([
        minX, 
        maxX
      ])
      .range([ 0, this.width ]);

    this.svg.append("g")
      .attr("transform", "translate(0," + this.height + ")")
      .call(d3.axisBottom(x));

    this.svg.append("text")             
      .attr("transform",
            "translate(" + (this.width/2) + " ," + 
                           (this.height + this.margin - 10) + ")")
      .style("text-anchor", "middle")
      .text(this.xLabel);

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([
        minY, 
        maxY
      ])
      .range([ this.height, 0]);
    this.svg.append("g")
      .call(d3.axisLeft(y).tickFormat(d3.format(".2f")));

    this.svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - this.margin - 3)
      .attr("x",0 - (this.height / 2))
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text(this.yLabel);    

    // Add dots
    this.svg.append('g')
      .selectAll("dot")
      .data(data)
      .enter()
      .append("circle")
        .attr("cx", function (d) { return x(d.x); } )
        .attr("cy", function (d) { return y(d.y); } )
        .attr("r", 3.5)
        .style("fill", "#69b3a2")
 
 }


}