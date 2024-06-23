pragma solidity ^0.8.0;

contract Wallet {
    address private owner;
    mapping (address => uint256) public balances;

    constructor() public {
        owner = msg.sender;
    }

    function deposit(uint256 amount) public {
        require(msg.sender == owner, "Only the owner can deposit funds");
        balances[owner] += amount;
    }

    function withdraw(uint256 amount) public {
        require(msg.sender == owner, "Only the owner can withdraw funds");
        balances[owner] -= amount;
    }

    function getBalance() public view returns (uint256) {
        return balances[owner];
    }
}
