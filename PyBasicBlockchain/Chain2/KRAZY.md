# MessagingBlockchain 📡🚀

*LET'S GET CRAZY WITH BLOCKCHAIN MESSAGING!*

## Known Bugs 🐞
- The current implementation has a known issue where the blockchain validation fails due to hash mismatches. For example:
```shell
Block 1 hash mismatch: 000056ccfdd3c323f561a7a5aa736b918ec8300190c7ad76f71a7cdff0af5a5a != 5c82a22c32bd3232f1d8fcb129198a3ab521041cbe52001a7339d0fa1cc1df1e
Is blockchain valid? False
```

- This bug affects the is_chain_valid method, and fixing it will involve troubleshooting the hash computation and block validation logic.


## Chat App Example 💬
*About the App*
- Real-Time Messaging App with MessagingBlockchain
- It uses socket connections to chat and PyBasicBlockchain2 to save the messages in a blockchain format in a .json file
*The application will include:*
  - A console interface for sending and receiving messages.
  - Real-time updates to show incoming messages.
*How to get the app*
- Navigate to `/Chain2/ChatApp` and there you go!
  - Two code files namely `ChatApp.py` and `ChatServer.py` will be there and the good old `PyBasicBlockchain2.py`
  - `ChatApp.py` is basically the chat client (User Interface).
  - `ChatServer.py` is the server.
*More on App*
  - Read the `/Chain2/ChatApp/CHATAPP.md` for more info!

## Conclusion 🎉
- These tests and the example chat app give you a solid starting point to explore the capabilities of the MessagingBlockchain class. Feel free to tweak the tests and app to better suit your needs. Happy testing and coding! 🚀💬
