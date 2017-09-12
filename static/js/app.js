var auctionApp = angular.module('auctionApp', []);

angular.module('auctionApp').controller('homePageController', function($scope, $rootScope, $http, $interval) {
    console.log("homePageController");
    
    $scope.showTimer = false;
    $scope.bidNow = function () {
        $scope.name = "";
        $scope.email = "";
        $scope.bidAmount = 0;
        $('#bidNowModal').modal();
    };
    
    $scope.submitBid = function () {
        console.log($scope.name);
        console.log($scope.email);
    }
    
    $scope.startTimer = function (startTime) {

        $scope.startTime = new Date(startTime);
        $scope.now = new Date();
        if ($scope.startTime - $scope.now > 1000) {
                        $scope.showTimer = true;
                        $scope.secondsRemaining = parseInt(($scope.startTime - $scope.now) / 1000);

                        $interval(function () {
                            $scope.secondsRemaining -=1;
                            if($scope.secondsRemaining > 0){
                                $scope.showTimer = true;
                            }else{
                                $scope.showTimer = false;
                            }
                        },1000);
                    }
        angular.element('.show-after-angular').removeClass('show-after-angular');


    }
});

auctionApp.run(function($rootScope, $http) {
    $rootScope.baseURL = '127.0.0.1:8000';

});
auctionApp.filter('secondsToDayHourMin', [function() {
    return function(seconds) {
        if(parseInt(seconds/(3600*24)) > 1){
            return parseInt(seconds/(3600*24))+' Days '+parseInt(seconds/3600)%24+' Hrs '+ parseInt(seconds/60)%60+' Min '+ seconds%60+' Sec';
        }else if(parseInt(seconds/(3600*24))>0){
            return parseInt(seconds/(3600*24))+' Day '+parseInt(seconds/3600)%24+' Hrs '+ parseInt(seconds/60)%60+' Min '+ seconds%60+' Sec';
        }else{
            return parseInt(seconds/3600)%24+' Hrs '+ parseInt(seconds/60)%60+' Min '+ seconds%60+' Sec';
        }

    };
}])
angular.module('auctionApp').config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

