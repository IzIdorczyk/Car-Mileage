import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {DashboardComponent} from "./pages/dashboard/dashboard.component";
import {CarsComponent} from "./pages/cars/cars.component";

const routes: Routes = [
    {path: "", component: DashboardComponent},
    {path: "cars", component: CarsComponent}];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {
}
