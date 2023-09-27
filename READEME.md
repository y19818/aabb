<!-- 这是一个注释
<div align="center">
  <a href="https://github.com/Sovereign-Labs/sovereign-sdk/blob/stable/LICENSE">
    <img alt="License: Apache-2.0" src="https://img.shields.io/github/license/Sovereign-Labs/sovereign-sdk.svg" />
  </a>
  <a href="https://discord.gg/kbykCcPrcA" > 
      <img alt="Discord" src="https://img.shields.io/discord/1050059327626555462?label=discord"/> 
  </a>
  <a href="https://codecov.io/gh/Sovereign-Labs/sovereign-sdk" > 
      <img alt="Coverage" src="https://codecov.io/gh/Sovereign-Labs/sovereign-sdk/branch/nightly/graph/badge.svg"/> 
  </a>
  <img alt="GitHub Workflow Status (with event)" src="https://img.shields.io/github/actions/workflow/status/Magport/Magnet/rust.yml?label=Pre-release%20checks">
</div>
 -->
## What is the MAGNET?


**MAGNET serves as Polkadot's Smart Contract Docking Station, operating on the PAYG Model. It is in the process of developing a scalable smart contract platform, utilizing DOT as the gas fee within this model.**

🔎 For more about Tanssi Network, head to our [website](https://magnet.magport.io/)<br>
📢 Follow our latest updates on [Twitter](https://twitter.com/Magnet20239)<br>
🤝 Engage with fellow developers on our [Telegram server](https://t.me/+aep298N0KXUwZTM1)<br>

### Business Model Introduction

The main roles involved in the business logic are as follows:
Tanssi Collators: As Magnet will become a ContainerChain in the
Tanssi Network, Collators will be elected and supported by the Tanssi
Network, and Magnet will no longer set up a Collators election
mechanism.

Magnet: As a smart contract platform, it provides EVM/WASM smart
contract services and charges GAS fees as platform fees.

Relaychain: Provides high-quality BlockSpace for Magnet and offers
blockchain security services

![Diagram of Magnet Operation](https://github.com/y19818/aabb/blob/master/DiagramofMagnetOperation.png)

### Magnet pallet introduction

Blockspace Ordering pallet:
1. Monitor Pool Gas
2. Monitor Polkadot CoreTime Price
3. Bidder Triggered, Transaction Added to Block, Block Production, Block Submission, Block Verification Locked
4. Gas Fee Revenue Credited to System Account
5. Invoke Profit Operator

Profit Operator pallet:
1. Confirm CoreTime cost
2. Calculate Block_Profit
3. Incremental Era_Cost
4. Incremental Era_Profit
5. Profit Distribution (Through incremental Era_Profit value, withdraw profit distribution from system account; negative numbers are not triggered)
6. Deposit Credit account based on the Incremental Era_Cost Value 
7. Triggered every era, or Triggered by other module

Blockspace/Coretime  Assurance Pallet:
1. Monitor Block Interval Time
2. Monitor Credit Account Balance
3. Trigger Order or Profit Distribution Upon Reaching Threshold


## Build the Magnet Node

To build Magnet, you will need a proper Substrate development environment.

If you need a refresher setting up your Substrate environment, see [Substrate's Getting Started Guide](https://substrate.dev/docs/en/knowledgebase/getting-started/).


## Getting Started


## Testing


## License

Licensed under the [Apache License, Version
2.0](./LICENSE).

Unless you explicitly state otherwise, any contribution intentionally submitted
for inclusion in this repository by you, as defined in the Apache-2.0 license, shall be
licensed as above, without any additional terms or conditions.
