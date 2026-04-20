const { rgb } = window.PDFLib;

// Name colours
export const NAME_COLOR_HONORARY = rgb(0.753, 0.004, 0); // #c00100 red honorary
export const NAME_COLOR_ANNIVERSARY = rgb(0.059, 0.408, 0.651); // #0f68a6 blue anniversary

// Asset paths — all relative to index.html
export const ASSETS = {
  template: "assets/template.pdf",
  templateHonorary: "assets/template_honorary.pdf",
  font: "assets/Diploma.ttf",
  seal: "assets/seal.png",
  starBronze: "assets/star_bronze.png",
  starSilver: "assets/star_silver.png",
  starGold: "assets/star_gold.png",
  blankScript: "assets/Blank%20Script.otf",
};
