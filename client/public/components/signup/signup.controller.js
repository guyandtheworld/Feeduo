signup
    .controller('SignupController', ['$scope','$log','$resource','userService',function($scope,$log,$resource,userService) {

        $scope.userList = [];

        $scope.sendData = function() {
        var user = {name:'jitin',number:'9339339383',email:'jaem@ga.com'};
        userService.add($scope.user);
    };
}])
    .factory('userService', function($resource) {
        return $resource(
            'http://192.168.1.65:8000/customers/',
            {},
            {
                'add': {
                    method: 'POST',
//                    isArray: true,
//                    headers: {
 //                       'Content-Type':'application/json'
//                        },
                }
            },
            {
 //               stripTrailingSlashes: false
            }
        );
    });
