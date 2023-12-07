import {Component, OnInit} from '@angular/core';

@Component({
  selector: 'app-nav-darkmode',
  standalone: true,
  imports: [],
  templateUrl: './nav-darkmode.component.html',
  styleUrl: './nav-darkmode.component.scss'
})
export class NavDarkmodeComponent implements OnInit {

  ngOnInit() {
    if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) &&
      window.matchMedia('(prefers-color-scheme: dark)').matches)) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark')
    }
  }
}
