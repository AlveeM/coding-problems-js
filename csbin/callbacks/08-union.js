function union(...arrays) {
    const set = arrays.reduce((acc, arr) => {
        arr.forEach(el => acc.add(el));
        return acc;
    }, new Set());
    return Array.from(set);
}

console.log(union([5, 10, 15], [15, 88, 1, 5, 7], [100, 15, 10, 1, 5]));
// should log: [5, 10, 15, 88, 1, 7, 100]