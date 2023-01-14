import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule, HttpTestingController } from '@angular/common/http/testing';
import { NoticiasService } from './noticias-service.service';

describe('NoticiasService', () => {
  let service: NoticiasService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule,
      ],
    });
    service = TestBed.inject(NoticiasService);
    const httpMock = TestBed.get(HttpTestingController); 
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
