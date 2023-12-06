import {Component, OnInit} from '@angular/core';

@Component({
    selector: 'app-darkmode-toggle',
    standalone: true,
    imports: [],
    templateUrl: './darkmode-toggle.component.html',
    styleUrl: './darkmode-toggle.component.scss'
})
export class DarkmodeToggleComponent implements OnInit {

    ngOnInit() {
        if (localStorage.getItem('color-theme') === 'dark' || (!('color-theme' in localStorage) &&
            window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.classList.add('dark');
        } else {
            document.documentElement.classList.remove('dark')
        }
    }



}
