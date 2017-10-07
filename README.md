# To

To is a bash tool to help you move around folders. Think of it as a powerful 'cd' alias.

## Usage

**to** is a bash tool to help you move around folders. It is specially useful when you need to constantly visit the same project folder. The main advantage of using **to** is to stop maitaining and hardcoding aliases in your `.bash_profile` or `.bashrc` file.

Let's start with a few examples:

Runnig: `to doc`
will take you to: **~/Documents**

Running `to de` will take you to: **~/Desktop**

Running `to pi` will take you to: **~/Pictures**

To go to **~/Repositories/my-cool-app/android/app/build/outputs/apk**

Just run: `to rmyaaboa`

Note that these are the minimum letters that you need to type in order to achieve an unambiguous `cd` command. So running only:
`to d` will print `['Downloads', 'Desktop', 'Documents']` so you can fix your input and remove ambiguity.


#### Pro tip:

**to** works even better if you can search through your bash history using your up and down arrows. You can achive that by adding into your `~/.inputrc` file the following lines:
```
"\e[A": history-search-backward
"\e[B": history-search-forward
set show-all-if-ambiguous on
set completion-ignore-case on
```

You need to restart your terminal after adding these lines in `.inputrc`.

After that, when you start typing a bash command: Ex. `git pull ori` and press *Up*, it will auto-complete with commands from your bash history that starts with `git pull ori`.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for usage and development purposes. Keep in mind that this is still very new, so expect some bugs. Please open issue when you find one and feel free to contribute!

### Prerequisites

```
Operating system:
- Linux or MacOS

Software:
- Python 2.x.x or Python 3.x.x (Already installed in both operating systems)
```

### Installing

Clone the project:

`git clone https://github.com/nmoya/to.git`

Go to the cloned folder and give permission to `install.sh`:

`chmod +x install.sh`

Run `./install.sh`

After these steps, **to** will be ready to use.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
