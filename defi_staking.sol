// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// 极简质押挖矿合约
contract DeFiStaking {
    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardToken;

    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public rewardDebt;

    uint256 public rewardRate = 100; // 每秒奖励
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    constructor(address _staking, address _reward) {
        stakingToken = IERC20(_staking);
        rewardToken = IERC20(_reward);
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        stakedBalance[msg.sender] += amount;
    }

    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakedBalance[msg.sender] >= amount, "Insufficient balance");
        stakedBalance[msg.sender] -= amount;
        stakingToken.transfer(msg.sender, amount);
    }

    function claimReward() external {
        uint256 reward = earned(msg.sender);
        require(reward > 0, "No reward to claim");
        rewardDebt[msg.sender] = rewardPerTokenStored;
        rewardToken.transfer(msg.sender, reward);
    }

    function earned(address account) public view returns (uint256) {
        return (stakedBalance[account] * (rewardPerTokenStored - rewardDebt[account])) / 1e18;
    }
}

interface IERC20 {
    function transferFrom(address, address, uint256) external returns (bool);
    function transfer(address, uint256) external returns (bool);
}
