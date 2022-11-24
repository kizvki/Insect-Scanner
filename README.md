<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/kizvki/Insect-Scanner">
    <img src="images/logo.jpg" alt="Logo" width="300" height="300">
  </a>

<h3 align="center">Insect scanner</h3>

  <p align="center">
    Script and documentation on scanning insects
    <br />
    <a href="https://apple-puppet-9e4.notion.site/Public-documentation-d2a36e2fab1b421ab56437c818de71e7"><strong>Explore the documentation »</strong></a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project<li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
Software:
* Disc3D
* Metashape

Hardware:
* Small world vision - [Insect scanner DISC3D](https://small-world-vision.de/en/)

### Installation

1. Download all the files inside corresponding Metashape version under 'Insect-Scanner/Metashape/Script/Version X.X/'
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
There are four different scripts:
* BatchScript <br>
process one insect to a 3d model.

* BatchScript_FastCalculation <br>
process one insect to a 3d model with the addition that the calculation will be approx. 3x faster with minmal loss of quality. Can be used for experimenting.

* Multi_BatchScript <br>
process mutiple insect to 3d models at once

* Model_Exporter <br>
export multiple insect 3d models to obj at once 

_For more informations, please refer to the [Documentation]([https://example.com](https://apple-puppet-9e4.notion.site/Public-documentation-d2a36e2fab1b421ab56437c818de71e7))_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Any contributions are greatly appreciated.

If you have a suggestion, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
Dr. Michael Greeff - michael.greeff@usys.ethz.ch
  
Ernst Herb - ernsthafter5@gmail.com

Christian Felsner - christian.felsner@gmail.com
  
<br />
<div align="center">
  <p align="center">
    <a href="https://github.com/kizvki/Insect-Scanner/issues">Report Bug</a>
    ·
    <a href="https://github.com/kizvki/Insect-Scanner/issues">Request Feature</a>
  </p>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
