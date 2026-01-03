#!/usr/bin/env -S deno run --allow-write --allow-read --allow-env
import { mix, opacity, shade, transparent } from "./utils.ts";
import { palettes, Handlebars, path } from "./palettes.ts";

Handlebars.registerHelper("opacity", opacity);
Handlebars.registerHelper("mix", mix);
Handlebars.registerHelper("shade", shade);
Handlebars.registerHelper("transparent", () => transparent);

const __dirname = path.dirname(path.fromFileUrl(import.meta.url));
const themePath = path.join(__dirname, "../themes/");
const uiPath = path.join(__dirname, "theme.json");
const uiMinimalPath = path.join(__dirname, "theme-minimal.json");
Deno.mkdirSync(themePath, {recursive: true});

const generate = (file_path: string, isMinimal: boolean) => {
	Deno.readTextFile(file_path).then((data: any) => {
		Object.entries(palettes).forEach(([key, value]) => {
			const hexValues = Object.entries(value)
				.map(([key, value]) => {
					return {
						[key]: value.hex.toUpperCase(),
					};
				})
				.reduce((acc, curr) => ({...acc, ...curr}), {});
			
			const options = {
				name: key + (isMinimal ? " Minimal" : ""),

				...hexValues,
			};

			const output = Handlebars.compile(data)(options);
			const fileName = key.split(" ").join("-").toLowerCase() + (isMinimal ? "-minimal" : "") + ".json";

			Deno.writeTextFileSync(path.join(themePath, fileName), output);
		});
	});
}

generate(uiPath, false);
generate(uiMinimalPath, true);
