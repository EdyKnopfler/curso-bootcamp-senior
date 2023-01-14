import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  login(username: String, password: String) {
    return this.http.post<any>(`/login`, { username, password })
            .pipe(map(resposta => {
                localStorage.setItem('token',resposta.access_token);
                this.token = resposta.access_token;
                return resposta;
            }));
  }

  token: String = "";

  constructor(private http: HttpClient) {
    this.token = "";
   }
}
