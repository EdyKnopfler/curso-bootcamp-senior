import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListaNoticiasComponent } from './lista-noticias/lista-noticias.component';
import { DetalheNoticiaComponent } from './detalhe-noticia/detalhe-noticia.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: '', component: ListaNoticiasComponent },
  { path: 'detalhes', component: DetalheNoticiaComponent },
  { path: 'login', component: LoginComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
