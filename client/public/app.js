'use strict';

var signup = angular.module("signup", []);
var home = angular.module("home", []);

angular
    .module('SampleApplication', [
        'appRoutes',
        'signup',
        'home',
        'ngResource'
    ])
    .config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);