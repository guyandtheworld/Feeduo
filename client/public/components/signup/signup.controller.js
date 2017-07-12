signup
    .controller('SignupController', ['$scope','$resource','userService', function($scope,$resource,userService) {
        $scope.message = "Hello World";

        $scope.sendData = function() {
        	userService.save({name:'jj', email:'jj@gmail.com',number:'9447220202'})
        }

}])
    .factory('userService', function($resource) {
        return $resource(
            'http://192.168.1.66:8000/customers/',
            {},
            {
            	'save': {
                    method: 'POST'
                	}

            });
    });