import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
})

export class AppService {

    constructor(private _http: HttpClient) { }

    getCurrencies() {
        return this._http.get("http://127.0.0.1:8000/currencies/")
            .pipe(map(result => result));
    }

    getCurrencyData(currency) {

        let data = { currency: currency }
        return this._http.post("http://127.0.0.1:8000/chartdata/", data)
            .pipe(map(result => result));
    }

}