'use strict';

var signup = angular.module("signup", []);
var home = angular.module("home", []);

angular
    .module('SampleApplication', [
        'appRoutes',
        'signup',
        'home'
    ]);