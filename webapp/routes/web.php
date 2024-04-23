<?php

use Illuminate\Support\Facades\Route; #(defecto)
#use IlluminateSupportFacadesRoute; (ejemplo no funciona)

Route::get('/', function () {
  $name = "John Doe";
  return view('welcome', ['name' => $name]);
});