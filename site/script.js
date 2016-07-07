var getRandomInt = function (min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};

var getContentDataAndType = (selectedFile,selectedConfigName,categoryBasePath) => {
  var contentData = "";
  var type = "text";

  if (selectedFile.text) {
    contentData = selectedFile.text;
    type = "text";
  }
  if (selectedFile.file) {
    contentData = categoryBasePath + selectedFile.file;
    if (selectedConfigName === "texts") {
      type = "markdown";
    } else {
      type = "image";
    }
  }
  if (selectedFile.url) {
    contentData = selectedFile.url;
    type = "image"
  }
  return {
    type: type,
    contentData: contentData
  }
};


var getIndex = function () {
  $.get("index.json", function (indexJson) {
    var basePath = indexJson.basePath;
    var configs = indexJson.configs;
    var randomIndex = getRandomInt(0, configs.length - 1);
    var selectedConfig = configs[randomIndex];
    var selectedConfigName = selectedConfig.name;
    var selectedCategoryFile = selectedConfig.file;

    $.get(basePath + selectedCategoryFile, function (categoryJson) {
      var categoryBasePath = categoryJson.basePath;
      var files = categoryJson.files;
      var randomFileIndex = getRandomInt(0, files.length - 1);
      var selectedFile = files[randomFileIndex];

      console.log(getContentDataAndType(selectedFile,selectedConfigName,categoryBasePath));
    });

  });
};

getIndex();
