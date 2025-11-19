# Solidity 基础学习

https://leapwhale.com/article/8r581039

## 合约结构

1. **SPDX 许可标识**：指定代码的开源许可。
2. **pragma 指令**：声明 Solidity 版本。
3. **导入语句**：引入其他合约或库。
4. **合约声明**：使用 `contract` 关键字。
5. **状态变量**：存储在区块链上的持久数据。
6. **事件**：用于记录重要操作，可被外部监听。
7. **修饰符**：用于修改函数行为的可重用代码。
8. **函数**：合约的可执行代码单元。

结构示例：

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 public storedData;

    constructor(uint256 initialValue) {
        storedData = initialValue;
    }

    function set(uint256 x) public {
        storedData = x;
    }

    function get() public view returns (uint256) {
        return storedData;
    }
}
```

## 数据类型与数据结构

Solidity 支持多种数据类型，包括基础类型（如 `uint`、`int`、`bool`）、复杂类型（如 `struct`、`enum`、数组、映射）以及地址类型 `address`。了解这些数据类型的特性对于编写高效和安全的合约至关重要。

**值类型**

- **uint**: 无符号整数，`uint256`是默认类型，表示 0 到 2^256-1 的整数。可以使用不同的位宽，如`uint8`、`uint16`等。
- **int**: 有符号整数，范围为-2^(n-1)到 2^(n-1)-1。
- **bool**: 布尔类型，只有`true`和`false`两个值。
- **address**: 20 字节的以太坊地址类型，分为`address`和`address payable`（后者可用于接收以太币）。
- **bytes1 ~ bytes32**：固定大小字节数组

**引用类型**

- **string**：动态大小的 UTF-8 编码字符串
- **bytes**：动态大小的字节数组
- **数组**：如 `uint[]`（动态大小）或 `uint[5]`（固定大小）
- **结构体 (Struct)**：自定义的复杂数据类型，例：`struct Person { string name; uint age; }`
- **映射 (Mapping)**：键值对存储，如 `mapping(address => uint)`

**注意事项**

- Mapping 不支持直接遍历，需结合其他结构记录键值。
- 动态数组操作（如`push`）会增加 Gas，尽量减少不必要的操作。

## 函数修饰符与类型

函数修饰符决定了函数的可见性和行为：

1. 可见性修饰符：
   - `public`：内部和外部都可调用
   - `private`：只能在定义的合约内部调用（虽然区块链上的数据是公开的，但限制了其他合约的直接访问）
   - `internal`：只能在内部和派生合约中调用
   - `external`：只能从外部调用
2. 状态修饰符：
   - `view`：不修改状态（但可以读取）
   - `pure`：不读取也不修改状态
3. 支付相关：
   - `payable`：允许函数接收以太币

**注意事项**

- 使用`private`并不意味着数据绝对安全，仍需注意数据泄露的可能性。
- `external`函数比`public`函数消耗更少 Gas，适用于只需外部访问的函数。
- `view`和 `pure` 声明的函数直接执行不会消耗 Gas，只是做了个调用，没有发送交易，但如果是别的需要消耗 Gas 的函数调用了 `view` 或者 `pure` 的函数，还是会消耗对应的 Gas 的。

## 内存管理与数据位置

Solidity 中的数据存储位置决定了数据的生命周期和 Gas 消耗：

- **Storage**: 永久存储，数据保存在区块链上。默认的状态变量存储位置，Gas 成本高。
- **Memory**: 临时数据位置，函数调用结束即释放。适合在函数内处理临时数据。
- **Calldata**: 只读数据位置，通常用于外部函数调用的参数。不可修改，效率高。

**注意事项**

- 尽量减少 Storage 的读写次数以节省 Gas。
- 在复杂数据操作中，优先考虑 Memory。
- 静态数据类型如固定大小的数组或基本类型不需要指定数据位置。
