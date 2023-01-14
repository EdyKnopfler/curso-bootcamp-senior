import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Noticia } from './noticias';

@Injectable({
  providedIn: 'root'
})
export class NoticiasService {

  constructor(private http: HttpClient) { 

  }

  getNoticias() {
    return this.http.get<Noticia[]>("/api/");
  }
}
