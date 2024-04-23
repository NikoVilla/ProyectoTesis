<?php

use Illuminate\Support\Facades\Route; #(defecto)
#use IlluminateSupportFacadesRoute; #(ejemplo no funciona)

Route::get('/', function () {
  $name = "Nicolas Villanueva";
  return view('welcome', ['name' => $name]);
});