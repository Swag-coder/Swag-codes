const sqr = [];
let int = 32;
for (let i = 2; i < Math.sqrt(n * 2); i++) {
    sqr.push(i * i);
}

const remaining = [];
for (let i = 2; i <= n; i++) {
    remaining.push(i);
}
const chain = [1];
let ind = 0;
let found = false;