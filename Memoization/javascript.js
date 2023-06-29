const gridTravelerMemoi = (m, n, memo={}) =>{

    const key = m + ',' + n;

    if(key in memo) return 1;
    

    if(m == 1 && n == 1) return 1;
    if(m == 0 || n == 0) return 0;


    memo[key] = gridTravelerMemoi(m-1, n, memo) + gridTravelerMemoi(m, n-1, memo)

    return memo[key]
};




console.log(gridTravelerMemoi(1, 1));
console.log(gridTravelerMemoi(2, 3));
console.log(gridTravelerMemoi(3, 2));
console.log(gridTravelerMemoi(3, 3)) ;
console.log(gridTravelerMemoi(18, 18));