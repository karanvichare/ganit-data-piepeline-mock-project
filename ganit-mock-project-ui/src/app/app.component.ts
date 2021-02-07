import { Component, ViewChild, ElementRef } from '@angular/core';
import { AppService } from './app.service';
import { Chart } from 'chart.js';

//@Component code removed for brevity
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  currencies = [];
  currency_data = [];
  title = 'ganit-mock-project-ui';
  chart: any = []; // This will hold our chart info
  @ViewChild('myCanvas')
  public canvas: ElementRef;
  public context: CanvasRenderingContext2D;
  public chartType: string = 'line';
  public chartData: any[];
  public chartLabels: any[];
  public chartColors: any[];
  public chartOptions: any;
  selectedCurrency = '';
  

  constructor(private api_service: AppService, private elementRef: ElementRef) { }

  ngOnInit() {
    this.api_service.getCurrencies()
      .subscribe(res => {
        console.log(res);
        this.currencies = res['currency_types'];
        console.log(this.currencies)
        this.selectedCurrency=res['currency_types'][0];
        this.getData(this.selectedCurrency) ;
      })
  };

  updateData(currency) {
    this.selectedCurrency=currency
    this.getData(currency)
  }
  getData(currency) {
    this.api_service.getCurrencyData(currency)
      .subscribe(res => {
        // console.log(res);
        this.currency_data = res['currency_types'];
        

        this.currency_data.sort((b, a) => new Date(b.date).getTime() - new Date(a.date).getTime());
        console.log(this.currency_data, "getCurrencyData")

        let result = this.currency_data.map(a => a.value);
        // let result = objArray.map(a => a.foo);

        // let data_max = Math.max( ...result );
        // let temp_min = this.data['list'].map(res => res.main.temp_min);
        let Dates = this.currency_data.map(a => a.date);
        console.log(Dates, "Dates")
        // let Dates = []
        // alldates.forEach((res) => {
        //   let jsdate = new Date(res * 1000)
        //   Dates.push(jsdate.toLocaleTimeString('en', { year: 'numeric', month: 'short', day: 'numeric' }))
        // })
        let htmlRef = this.elementRef.nativeElement.querySelector(`#canvas`);
        this.chart = new Chart(htmlRef, {
          type: 'line',
          data: {
            labels: Dates,
            datasets: [
              {
                data: result,
                borderColor: "#3cba9f",
                fill: false
              },
              // {
              //   data: temp_min,
              //   borderColor: "#ffcc00",
              //   fill: false
              // },
            ]
          },
          options: {
            legend: {
              display: false
            },
            scales: {
              xAxes: [{
                display: true
              }],
              yAxes: [{
                display: true
              }],
            }
          }
        });
      })
  }


}