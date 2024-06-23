const { deployer, web3 } = require('@openzeppelin/truffle-deployer');

module.exports = async function(deployer) {
  await deployer.deploy(Blockchain);
  await deployer.deploy(Wallet);
};
