angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'signup',
        url: '/',
        templateUrl: 'public/components/signup/signup.template.html',
        controller: 'SignupController'
    });

    $urlRouterProvider.otherwise('/');
}]);