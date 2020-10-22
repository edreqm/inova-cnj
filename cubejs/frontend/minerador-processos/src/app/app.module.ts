import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { CubejsClientModule } from '@cubejs-client/ngx';
import { HeatMapComponent } from './heat-map/heat-map.component';
import { SelecaoLitiganteComponent } from './selecao-litigante/selecao-litigante.component'

const cubejsOptions = /*{
  token:
    "2952749ef5df99ae7d33889219988c03414b66154dc17a2458d520bad9762150ce37cac356a738c4a4644442bb47c74855168aa023645fea366ca511ee86ca08",
  options: {
    apiUrl: "http://localhost:4000/cubejs-api/v1"
  }
};*/
{
  token:
    "2952749ef5df99ae7d33889219988c03414b66154dc17a2458d520bad9762150ce37cac356a738c4a4644442bb47c74855168aa023645fea366ca511ee86ca08",
  options: {
    apiUrl: "https://analise-litigantes-back.herokuapp.com/cubejs-api/v1"
  }
};

@NgModule({
  declarations: [
    AppComponent,
    HeatMapComponent,
    SelecaoLitiganteComponent
  ],
  imports: [
    BrowserModule,
    CubejsClientModule.forRoot(cubejsOptions)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
