import { ComponentFixture, TestBed } from '@angular/core/testing';
import { NoticiasService } from '../noticias-service.service';
import { ListaNoticiasComponent } from './lista-noticias.component';
import { of } from 'rxjs';

describe('ListaNoticiasComponent', () => {
  let component: ListaNoticiasComponent;
  let fixture: ComponentFixture<ListaNoticiasComponent>;
  let noticiasServiceMock: any;
  const listaNoticiasFake$ = {
    "_embedded" : {
      "api" : {
        id : 1,
        titulo : "Titulo fake 1",
        resumo : "Resumo fake 1",
        thumb : "",
        imagem : "",
        texto : "Texto fake 1",
        data : new Date()
      }
    }
  }

  beforeEach(async () => {
    noticiasServiceMock = jasmine.createSpyObj(['getNoticias']);
    const list$ = jasmine.createSpy().and.returnValue(listaNoticiasFake$);
    noticiasServiceMock.getNoticias.and.returnValue(of(list$));

    await TestBed.configureTestingModule({
      declarations: [ ListaNoticiasComponent ],
      providers: [ { provide: NoticiasService, useValue: noticiasServiceMock } ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ListaNoticiasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {  
    expect(component).toBeTruthy();
  });
});
