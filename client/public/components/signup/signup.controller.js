signup
    .controller('SignupController', ['$scope','$log','$resource','userService',function($scope,$log,$resource,userService) {


        $scope.sendData = function() {
        var user = {name:'jitin',number:'9339339383',email:'jaem@ga.com'};
        $scope.userList = userService.add($scope.user,{},function (respond){
            console.log(respond);
        },
        function(error){
            console.log(error);
        });
    };
}])
    .factory('userService', function($resource) {
        return $resource(
            'https://jsonplaceholder.typicode.com/users/',
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

//     .../id/chain   json