// SPDX-License-Identifier: MIT
// Proyecto blockchain
// Desarrollado por Ricardo Rosero - n4p5t3r
// Email: rrosero2000@gmail.com
// Coins ICO

// Versión del compilador
pragma solidity ^0.8.18;

contract CoinICO {
    // Numero maximo de monedas a la venta
    uint256 public maxCoins = 1000000;

    // Tasa de conversion USD a RRC
    uint256 public usdToCoin = 1000;

    // Numero total de monedas compradas
    uint256 public totalCoinsBought;

    // Mapeo de direccion de inversionista a monedas
    mapping(address => uint256) public equityCoins;
    mapping(address => uint256) public equityUSD;

    // Modificador: verificar si un inversionista puede comprar monedas
    modifier canBuyCoins(uint256 usdInvested) {
        require(usdInvested * usdToCoin + totalCoinsBought <= maxCoins, "No hay suficientes monedas disponibles");
        _;
    }
    
    // Obtener capital invertido en monedas
    function equityInCoins(address investor) external view returns (uint256) {
        return equityCoins[investor];
    }

    // Obtener capital invertido en dolares USD
    function equityInUSD(address investor) external view returns (uint256) {
        return equityUSD[investor];
    }

    // Comprar monedas
    function buyCoins(address investor, uint256 usdInvested) external canBuyCoins(usdInvested) {
        uint256 coinsBought = usdInvested * usdToCoin;
        equityCoins[investor] += coinsBought;
        equityUSD[investor] = equityCoins[investor] / 1000;
        totalCoinsBought += coinsBought;
    }

    // Vender monedas
    function sellCoins(address investor, uint256 coinsSold) external {
        equityCoins[investor] -= coinsSold;
        equityUSD[investor] = equityCoins[investor] / 1000;
        totalCoinsBought -= coinsSold;
    }
}
