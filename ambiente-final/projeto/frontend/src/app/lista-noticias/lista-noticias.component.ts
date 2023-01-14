import { Component, OnInit } from '@angular/core';
import { Noticia } from '../noticias';
import { HttpClient } from '@angular/common/http';
import { NoticiasService } from '../noticias-service.service';

@Component({
  selector: 'app-lista-noticias',
  templateUrl: './lista-noticias.component.html',
  styleUrls: ['./lista-noticias.component.css']
})
export class ListaNoticiasComponent implements OnInit {
  
  noticias!: Noticia[];

  constructor(private noticiasService: NoticiasService) { }

  ngOnInit(): void {
    this.noticias = [];
    this.noticiasService.getNoticias()
      .subscribe((dados: any) => this.noticias = dados._embedded.api);
  }

}
