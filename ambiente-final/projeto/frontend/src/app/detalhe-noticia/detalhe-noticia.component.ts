import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router, NavigationStart } from '@angular/router';
import { Location } from '@angular/common';
import { Noticia } from '../noticias';

@Component({
  selector: 'app-detalhe-noticia',
  templateUrl: './detalhe-noticia.component.html',
  styleUrls: ['./detalhe-noticia.component.css']
})
export class DetalheNoticiaComponent implements OnInit {
  noticia!: Noticia;

  constructor(private router:Router, private activatedRoute:ActivatedRoute,
    private location: Location) {}

  ngOnInit(): void {
    this.noticia = history.state;
    console.log(this.noticia);
  }

  voltar(): void {
    this.location.back();
  }

}
