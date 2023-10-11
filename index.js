const fs = require("fs");

const processWords = (lib) =>
  Object.entries(lib)
    .map(([k, v]) => [k, v.definition])
    .filter(([k, v]) => !v.includes("см. "))
    .filter(([k, v]) => !v.includes("Отвлеч. сущ. по знач. прил."))
    .filter(([k, v]) => !v.includes("Процесс действия по знач. несов. глаг."))
    .filter(([k, v]) => !v.includes("Процесс действия по знач. глаг."))
    .filter(([k, v]) => !v.includes("Действие по знач. глаг."))
    .filter(([k, v]) => !v.includes("Уничик сущ."))
    .filter(([k, v]) => !v.includes("Женск. к сущ."))
    .filter(([k, v]) => !v.includes("Мужск. к сущ."))
    .filter(([k, v]) => !v.includes("Уменьш. к сущ."))
    .filter(([k, v]) => !v.includes("Ласк. к сущ."))
    .filter(([k, v]) => !v.includes("То же, что"))
    .map(([k, v]) => [k, v.replace(/[мж]\. /g, "")])
    .map(([k, v]) => [k, v.replace(/устар\. /g, "")])
    .map(([k, v]) => [k, v.replace(/мн\. /g, "")])
    .map(([k, v]) => [k, v.replace(/прил\. /g, "")])
    .map(([k, v]) => [k, v.replace(/\([\d]\*\)/g, "")])
    .map(([k, v]) => [k, v.replace(/перен\. /g, "")])
    .map(([k, v]) => [k, v.replace(/разг\. /g, "")])
    .map(([k, v]) => [k, v.replace(/нескл\. /g, "")])
    .map(([k, v]) => [k, v.replace(/нареч\. /g, "")])
    .map(([k, v]) => [k, v.replace(/местн\. /g, "")])
    .map(([k, v]) => [k, v.replace(/ср\. /g, "")])
    .map(([k, v]) => [k, v.replace(/ \([\d]\)/g, "")])
    .map(([k, v]) => [k, v.replace(/[\d]\. /g, "")])
    .map(([k, v]) => [k, v.split(/[\d]\) /).filter((v) => v)]);

fs.writeFileSync("words", JSON.stringify(processWords(JSON.parse(fs.readFileSync("./words.json")))));
