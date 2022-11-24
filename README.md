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
We are in a process of digitalizing our [Entomological Collection](https://usys.ethz.ch/en/research/collections/entomological-collection.html). To optimize the process we are doing experiments and writing scripts to automate most of the process. In this documentation we are sharing our scripts and process optimaziations. It is important to note that the hardware with which the images are made to process the 3d model is from [Small World Vision](https://small-world-vision.de/en/). The informations gathered from the hardware are needed for most of the scripts.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps below.

### Prerequisites

Software:
* Disc3D
* Metashape

Hardware:
* Small world vision - [Insect scanner DISC3D](https://small-world-vision.de/en/)

### Installation

Download all the files for corresponding Metashape version under 'Insect-Scanner/Metashape/Script/Version X.X/'. Or you can simply download it [here](https://downgit.github.io/#/home?url=https://github.com/kizvki/Insect-Scanner/tree/main/Metashape/Script).<br>
Save the folder with the same folder strucutre where the .py files are contained.

  
Calibration:
  
1. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Install NPM packages
   ```sh
   npm install
   ```
3. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
To run the scripts you have to start them inside of Metashape:
1. Go to Tools>Run Script (Shortcut: Ctrl+R)
2. Select the folder icon
3. Browse for the desired script and open it
4. Press OK

The script will not go through and ask for the specified folder. 
  
<br>
  
There are four different scripts:
* **BatchScript** <br>
process one insect to a 3d model.

* **BatchScript_FastCalculation** <br>
process one insect to a 3d model with the addition that the calculation will be approx. 3x faster with minmal loss of quality. Can be used for experimenting.

* **Multi_BatchScript** <br>
process mutiple insect to 3d models at once

* **Model_Exporter** <br>
export multiple insect 3d models to obj at once 
  
_For more informations, please refer to the [Documentation](https://apple-puppet-9e4.notion.site/Public-documentation-d2a36e2fab1b421ab56437c818de71e7)_

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
  
Ernst Herb - ernsthxz@gmail.com

Christian Felsner - christian.felsner@usys.ethz.ch
  
<br />
<div align="center">
  <p align="center">
    <a href="https://github.com/kizvki/Insect-Scanner/issues">Report Bug</a>
    ·
    <a href="https://github.com/kizvki/Insect-Scanner/issues">Request Feature</a>
  </p>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
