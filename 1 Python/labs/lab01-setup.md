1. Create a new repository in GitHub [tutorial](https://docs.github.com/en/github/getting-started-with-github/create-a-repo) named something like "PDX Code Guild - Python Fullstack Solutions".
2. Open Visual Studio Code and open a new terminal from the main menu `Terminal -> New Terminal`
3. `cd` to a good directory store your source code (like `Desktop`, or `user/programs`), and run `git clone <repo url>`. This will create a local copy of your repository. Do `ls` to see the new folder.
4. Open that folder in Visual Studio Code from the main menu `File -> Open Folder`, or if VSCode is installed to PATH, you can open VSCode in your terminal using the command `code <foldername>`.
5. Using the `Explorer` on the left, create a new folder `solutions`.
6. Inside that folder create `1-hello_world.py`, write `print('hello world!')` inside the file, and save it.
7. In the top-right corner, you should see a green arrow, press that to run the file. Alternatively, open a terminal, `cd` into the `solutions` folder, `python 1-hello_world.py`. You should see "hello world!" in the terminal.
9. Use the GUI or terminal to commit the change and push it to the repository on GitHub
  1. `git pull`
  2. `git add 1-hello_world.py`
  3. `git commit -m "added hello world"`
  4. `git push`
10. Go to the repository on GitHub and you should see your file.