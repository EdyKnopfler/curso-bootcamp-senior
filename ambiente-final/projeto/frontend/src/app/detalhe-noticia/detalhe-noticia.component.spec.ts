import { ComponentFixture, TestBed } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { DetalheNoticiaComponent } from './detalhe-noticia.component';
import { Noticia } from '../noticias'; // Aqui
import { ListaNoticiasComponent } from '../lista-noticias/lista-noticias.component';
import { DebugElement } from '@angular/core';

describe('DetalheNoticiaComponent', () => {
  let component: DetalheNoticiaComponent;
  let fixture: ComponentFixture<DetalheNoticiaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RouterTestingModule.withRoutes([
        { path: '', component: ListaNoticiasComponent },
        { path: 'detalhes', component: DetalheNoticiaComponent }
      ])],
      declarations: [ DetalheNoticiaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(DetalheNoticiaComponent);
    component = fixture.componentInstance;
    // AQUI: 
    const noticia_init = <Noticia> {
      data: new Date(),
      id: 0,
      resumo: "resumo teste",
      texto: "texto teste",
      imagem: "",
      thumb: "",
      titulo: "titulo teste"
    };
    history.pushState(noticia_init,"","");
    fixture.detectChanges();

    
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have noticias date', () => {
    const dtdebug: DebugElement = fixture.debugElement;
    const dtel: HTMLElement = dtdebug.nativeElement;
    const p = dtel.querySelector('#dtnoticia')!;
    const dtTeste = new Date();
    const strDt = dtTeste.toLocaleString()
    expect(p.textContent?.trim()).toEqual(strDt);
  })

  it('should have noticias text', () => {
    const dtdebug: DebugElement = fixture.debugElement;
    const dtel: HTMLElement = dtdebug.nativeElement;
    const p = dtel.querySelector('#corponoticia')!;
    expect(p.textContent?.trim()).toEqual("texto teste");
  })
});
