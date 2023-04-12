//SPDX-License-Identifier: MIT
// Proyecto blockchain
// Desarrollado por Ricardo Rosero - n4p5t3r
// Email: rrosero2000@gmail.com
// Coins ICO

// Version del compilador
pragma solidity ^0.8.18;

contract coin_ico{
    // Introduciendo el numero maximo de coins a la venta
    uint public max_coins = 1000000;

    // Tasa de conversion USD a RRC
    uint public usd_to_coin = 1000;

    // Introduciendo numero total de coins
    uint public total_coins_bought = 0;

    // Mapeo de direccion de inversionista a coins
    mapping(address => uint)equity_coins;
    mapping(address => uint)equity_usd;

    // Verificando si un inversionista puede comprar coins
    modifier can_buy_coins(uint usd_invested){
        require(usd_invested * usd_to_coin + total_coins_bought <= max_coins);
        _;
    }
    
    // Obteniendo capital invertido en tokens
    function equity_in_coins(address investor)external view returns (uint) {
        return equity_coins[investor];
    }

    // Obteniendo capital invertido en dolares usd
    function equity_in_usd(address investor)external view returns (uint) {
        return equity_usd[investor];
    }

    // Comprando tokens
    function buy_coins(address investor, uint usd_invested) external can_buy_coins(usd_invested){
        uint coins_bought = usd_invested * usd_to_coin;
        equity_coins[investor] += coins_bought;

        equity_usd[investor] = equity_coins[investor] / 1000;

        total_coins_bought += coins_bought;
    }

    // Vendiendo tokens
    function sell_coins(address investor, uint coins_sold) external {
        equity_coins[investor] -= coins_sold;

        equity_usd[investor] = equity_coins[investor] / 1000;

        total_coins_bought -= coins_sold;
    }
}