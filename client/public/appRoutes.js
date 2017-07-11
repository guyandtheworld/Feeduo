angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', '$locationProvider', function($stateProvider, $urlRouterProvider, $locationProvider) {

    $stateProvider.state({
        name: 'signup',
        url: '/signup',
        templateUrl: 'public/components/signup/signup.template.html',
        controller: 'SignupController'
    });

    $stateProvider.state({
        name: 'home',
        url: '/',
        templateUrl: 'public/components/home/home.template.html',
        controller: 'HomeController'
    });

    $urlRouterProvider.otherwise('/');
    $locationProvider.html5Mode(true);
}]);