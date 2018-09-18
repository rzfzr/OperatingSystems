let HEAP = [];

const A = {
  language: 'JavaScript'
};

HEAP.push(A);

const root = () => HEAP[0];

const B = {
  language: 'Rust'
};

HEAP.push(B);

A.B = B;

const C = {
  language: 'Elm'
};

HEAP.push(C);

A.C = C;


const D = {
  language: 'GoLang'
};

HEAP.push(D);

B.D = D;

delete A.C;

delete A.B;

const gc = () => {
  mark();
  sweep();
}

const mark = () => {
  let reachables = [ root() ];
  
  while (reachables.length) {
    let current = reachables.pop();
    if (!current.__markBit__) {
      current.__markBit__ = 1;
      for (let i in current) {
        if (typeof current[i] === 'object') {
          reachables.push(current[i]);
        }
      }
    }
  }
}

const sweep = () => {
  HEAP = HEAP.filter((current) => {
    if (current.__markBit__ === 1) {
      current.__markBit__ = 0;
      return true;
    } else return false; // move it to the free list
  });
}
const main = () => {
  console.log("\nAntes: ", HEAP);
  gc();
  console.log("\nDepois: ", HEAP);
}
main();