#!/usr/bin/node

exports.logMe = (function () {
  let narg = 0;

  return (item) => {
    console.log(`${narg}: ${item}`);
    narg++;
  };
})();
