var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __commonJS = (cb, mod) => function __require() {
  return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
};
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, { get: all[name], enumerable: true });
};
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));
var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

// node_modules/obsidian-daily-notes-interface/dist/main.js
var require_main = __commonJS({
  "node_modules/obsidian-daily-notes-interface/dist/main.js"(exports) {
    "use strict";
    Object.defineProperty(exports, "__esModule", { value: true });
    var obsidian = require("obsidian");
    var DEFAULT_DAILY_NOTE_FORMAT = "YYYY-MM-DD";
    var DEFAULT_WEEKLY_NOTE_FORMAT = "gggg-[W]ww";
    var DEFAULT_MONTHLY_NOTE_FORMAT = "YYYY-MM";
    var DEFAULT_QUARTERLY_NOTE_FORMAT = "YYYY-[Q]Q";
    var DEFAULT_YEARLY_NOTE_FORMAT = "YYYY";
    function shouldUsePeriodicNotesSettings(periodicity) {
      var _a, _b;
      const periodicNotes = window.app.plugins.getPlugin("periodic-notes");
      return periodicNotes && ((_b = (_a = periodicNotes.settings) == null ? void 0 : _a[periodicity]) == null ? void 0 : _b.enabled);
    }
    function getDailyNoteSettings2() {
      var _a, _b, _c, _d;
      try {
        const { internalPlugins, plugins } = window.app;
        if (shouldUsePeriodicNotesSettings("daily")) {
          const { format: format2, folder: folder2, template: template2 } = ((_b = (_a = plugins.getPlugin("periodic-notes")) == null ? void 0 : _a.settings) == null ? void 0 : _b.daily) || {};
          return {
            format: format2 || DEFAULT_DAILY_NOTE_FORMAT,
            folder: (folder2 == null ? void 0 : folder2.trim()) || "",
            template: (template2 == null ? void 0 : template2.trim()) || ""
          };
        }
        const { folder, format, template } = ((_d = (_c = internalPlugins.getPluginById("daily-notes")) == null ? void 0 : _c.instance) == null ? void 0 : _d.options) || {};
        return {
          format: format || DEFAULT_DAILY_NOTE_FORMAT,
          folder: (folder == null ? void 0 : folder.trim()) || "",
          template: (template == null ? void 0 : template.trim()) || ""
        };
      } catch (err) {
        console.info("No custom daily note settings found!", err);
      }
    }
    function getWeeklyNoteSettings() {
      var _a, _b, _c, _d, _e, _f, _g;
      try {
        const pluginManager = window.app.plugins;
        const calendarSettings = (_a = pluginManager.getPlugin("calendar")) == null ? void 0 : _a.options;
        const periodicNotesSettings = (_c = (_b = pluginManager.getPlugin("periodic-notes")) == null ? void 0 : _b.settings) == null ? void 0 : _c.weekly;
        if (shouldUsePeriodicNotesSettings("weekly")) {
          return {
            format: periodicNotesSettings.format || DEFAULT_WEEKLY_NOTE_FORMAT,
            folder: ((_d = periodicNotesSettings.folder) == null ? void 0 : _d.trim()) || "",
            template: ((_e = periodicNotesSettings.template) == null ? void 0 : _e.trim()) || ""
          };
        }
        const settings = calendarSettings || {};
        return {
          format: settings.weeklyNoteFormat || DEFAULT_WEEKLY_NOTE_FORMAT,
          folder: ((_f = settings.weeklyNoteFolder) == null ? void 0 : _f.trim()) || "",
          template: ((_g = settings.weeklyNoteTemplate) == null ? void 0 : _g.trim()) || ""
        };
      } catch (err) {
        console.info("No custom weekly note settings found!", err);
      }
    }
    function getMonthlyNoteSettings() {
      var _a, _b, _c, _d;
      const pluginManager = window.app.plugins;
      try {
        const settings = shouldUsePeriodicNotesSettings("monthly") && ((_b = (_a = pluginManager.getPlugin("periodic-notes")) == null ? void 0 : _a.settings) == null ? void 0 : _b.monthly) || {};
        return {
          format: settings.format || DEFAULT_MONTHLY_NOTE_FORMAT,
          folder: ((_c = settings.folder) == null ? void 0 : _c.trim()) || "",
          template: ((_d = settings.template) == null ? void 0 : _d.trim()) || ""
        };
      } catch (err) {
        console.info("No custom monthly note settings found!", err);
      }
    }
    function getQuarterlyNoteSettings() {
      var _a, _b, _c, _d;
      const pluginManager = window.app.plugins;
      try {
        const settings = shouldUsePeriodicNotesSettings("quarterly") && ((_b = (_a = pluginManager.getPlugin("periodic-notes")) == null ? void 0 : _a.settings) == null ? void 0 : _b.quarterly) || {};
        return {
          format: settings.format || DEFAULT_QUARTERLY_NOTE_FORMAT,
          folder: ((_c = settings.folder) == null ? void 0 : _c.trim()) || "",
          template: ((_d = settings.template) == null ? void 0 : _d.trim()) || ""
        };
      } catch (err) {
        console.info("No custom quarterly note settings found!", err);
      }
    }
    function getYearlyNoteSettings() {
      var _a, _b, _c, _d;
      const pluginManager = window.app.plugins;
      try {
        const settings = shouldUsePeriodicNotesSettings("yearly") && ((_b = (_a = pluginManager.getPlugin("periodic-notes")) == null ? void 0 : _a.settings) == null ? void 0 : _b.yearly) || {};
        return {
          format: settings.format || DEFAULT_YEARLY_NOTE_FORMAT,
          folder: ((_c = settings.folder) == null ? void 0 : _c.trim()) || "",
          template: ((_d = settings.template) == null ? void 0 : _d.trim()) || ""
        };
      } catch (err) {
        console.info("No custom yearly note settings found!", err);
      }
    }
    function join(...partSegments) {
      let parts = [];
      for (let i = 0, l = partSegments.length; i < l; i++) {
        parts = parts.concat(partSegments[i].split("/"));
      }
      const newParts = [];
      for (let i = 0, l = parts.length; i < l; i++) {
        const part = parts[i];
        if (!part || part === ".")
          continue;
        else
          newParts.push(part);
      }
      if (parts[0] === "")
        newParts.unshift("");
      return newParts.join("/");
    }
    function basename(fullPath) {
      let base = fullPath.substring(fullPath.lastIndexOf("/") + 1);
      if (base.lastIndexOf(".") != -1)
        base = base.substring(0, base.lastIndexOf("."));
      return base;
    }
    async function ensureFolderExists(path) {
      const dirs = path.replace(/\\/g, "/").split("/");
      dirs.pop();
      if (dirs.length) {
        const dir = join(...dirs);
        if (!window.app.vault.getAbstractFileByPath(dir)) {
          await window.app.vault.createFolder(dir);
        }
      }
    }
    async function getNotePath(directory, filename) {
      if (!filename.endsWith(".md")) {
        filename += ".md";
      }
      const path = obsidian.normalizePath(join(directory, filename));
      await ensureFolderExists(path);
      return path;
    }
    async function getTemplateInfo(template) {
      const { metadataCache, vault } = window.app;
      const templatePath = obsidian.normalizePath(template);
      if (templatePath === "/") {
        return Promise.resolve(["", null]);
      }
      try {
        const templateFile = metadataCache.getFirstLinkpathDest(templatePath, "");
        const contents = await vault.cachedRead(templateFile);
        const IFoldInfo = window.app.foldManager.load(templateFile);
        return [contents, IFoldInfo];
      } catch (err) {
        console.error(`Failed to read the daily note template '${templatePath}'`, err);
        new obsidian.Notice("Failed to read the daily note template");
        return ["", null];
      }
    }
    function getDateUID(date, granularity = "day") {
      const ts = date.clone().startOf(granularity).format();
      return `${granularity}-${ts}`;
    }
    function removeEscapedCharacters(format) {
      return format.replace(/\[[^\]]*\]/g, "");
    }
    function isFormatAmbiguous(format, granularity) {
      if (granularity === "week") {
        const cleanFormat = removeEscapedCharacters(format);
        return /w{1,2}/i.test(cleanFormat) && (/M{1,4}/.test(cleanFormat) || /D{1,4}/.test(cleanFormat));
      }
      return false;
    }
    function getDateFromFile(file, granularity) {
      return getDateFromFilename(file.basename, granularity);
    }
    function getDateFromPath(path, granularity) {
      return getDateFromFilename(basename(path), granularity);
    }
    function getDateFromFilename(filename, granularity) {
      const getSettings = {
        day: getDailyNoteSettings2,
        week: getWeeklyNoteSettings,
        month: getMonthlyNoteSettings,
        quarter: getQuarterlyNoteSettings,
        year: getYearlyNoteSettings
      };
      const format = getSettings[granularity]().format.split("/").pop();
      const noteDate = window.moment(filename, format, true);
      if (!noteDate.isValid()) {
        return null;
      }
      if (isFormatAmbiguous(format, granularity)) {
        if (granularity === "week") {
          const cleanFormat = removeEscapedCharacters(format);
          if (/w{1,2}/i.test(cleanFormat)) {
            return window.moment(
              filename,
              // If format contains week, remove day & month formatting
              format.replace(/M{1,4}/g, "").replace(/D{1,4}/g, ""),
              false
            );
          }
        }
      }
      return noteDate;
    }
    var DailyNotesFolderMissingError = class extends Error {
    };
    async function createDailyNote(date) {
      const app = window.app;
      const { vault } = app;
      const moment2 = window.moment;
      const { template, format, folder } = getDailyNoteSettings2();
      const [templateContents, IFoldInfo] = await getTemplateInfo(template);
      const filename = date.format(format);
      const normalizedPath = await getNotePath(folder, filename);
      try {
        const createdFile = await vault.create(normalizedPath, templateContents.replace(/{{\s*date\s*}}/gi, filename).replace(/{{\s*time\s*}}/gi, moment2().format("HH:mm")).replace(/{{\s*title\s*}}/gi, filename).replace(/{{\s*(date|time)\s*(([+-]\d+)([yqmwdhs]))?\s*(:.+?)?}}/gi, (_, _timeOrDate, calc, timeDelta, unit, momentFormat) => {
          const now = moment2();
          const currentDate = date.clone().set({
            hour: now.get("hour"),
            minute: now.get("minute"),
            second: now.get("second")
          });
          if (calc) {
            currentDate.add(parseInt(timeDelta, 10), unit);
          }
          if (momentFormat) {
            return currentDate.format(momentFormat.substring(1).trim());
          }
          return currentDate.format(format);
        }).replace(/{{\s*yesterday\s*}}/gi, date.clone().subtract(1, "day").format(format)).replace(/{{\s*tomorrow\s*}}/gi, date.clone().add(1, "d").format(format)));
        app.foldManager.save(createdFile, IFoldInfo);
        return createdFile;
      } catch (err) {
        console.error(`Failed to create file: '${normalizedPath}'`, err);
        new obsidian.Notice("Unable to create new file.");
      }
    }
    function getDailyNote(date, dailyNotes) {
      var _a;
      return (_a = dailyNotes[getDateUID(date, "day")]) != null ? _a : null;
    }
    function getAllDailyNotes() {
      const { vault } = window.app;
      const { folder } = getDailyNoteSettings2();
      const dailyNotesFolder = vault.getAbstractFileByPath(obsidian.normalizePath(folder));
      if (!dailyNotesFolder) {
        throw new DailyNotesFolderMissingError("Failed to find daily notes folder");
      }
      const dailyNotes = {};
      obsidian.Vault.recurseChildren(dailyNotesFolder, (note) => {
        if (note instanceof obsidian.TFile) {
          const date = getDateFromFile(note, "day");
          if (date) {
            const dateString = getDateUID(date, "day");
            dailyNotes[dateString] = note;
          }
        }
      });
      return dailyNotes;
    }
    var WeeklyNotesFolderMissingError = class extends Error {
    };
    function getDaysOfWeek() {
      const { moment: moment2 } = window;
      let weekStart = moment2.localeData()._week.dow;
      const daysOfWeek = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday"
      ];
      while (weekStart) {
        daysOfWeek.push(daysOfWeek.shift());
        weekStart--;
      }
      return daysOfWeek;
    }
    function getDayOfWeekNumericalValue(dayOfWeekName) {
      return getDaysOfWeek().indexOf(dayOfWeekName.toLowerCase());
    }
    async function createWeeklyNote(date) {
      const { vault } = window.app;
      const { template, format, folder } = getWeeklyNoteSettings();
      const [templateContents, IFoldInfo] = await getTemplateInfo(template);
      const filename = date.format(format);
      const normalizedPath = await getNotePath(folder, filename);
      try {
        const createdFile = await vault.create(normalizedPath, templateContents.replace(/{{\s*(date|time)\s*(([+-]\d+)([yqmwdhs]))?\s*(:.+?)?}}/gi, (_, _timeOrDate, calc, timeDelta, unit, momentFormat) => {
          const now = window.moment();
          const currentDate = date.clone().set({
            hour: now.get("hour"),
            minute: now.get("minute"),
            second: now.get("second")
          });
          if (calc) {
            currentDate.add(parseInt(timeDelta, 10), unit);
          }
          if (momentFormat) {
            return currentDate.format(momentFormat.substring(1).trim());
          }
          return currentDate.format(format);
        }).replace(/{{\s*title\s*}}/gi, filename).replace(/{{\s*time\s*}}/gi, window.moment().format("HH:mm")).replace(/{{\s*(sunday|monday|tuesday|wednesday|thursday|friday|saturday)\s*:(.*?)}}/gi, (_, dayOfWeek, momentFormat) => {
          const day = getDayOfWeekNumericalValue(dayOfWeek);
          return date.weekday(day).format(momentFormat.trim());
        }));
        window.app.foldManager.save(createdFile, IFoldInfo);
        return createdFile;
      } catch (err) {
        console.error(`Failed to create file: '${normalizedPath}'`, err);
        new obsidian.Notice("Unable to create new file.");
      }
    }
    function getWeeklyNote(date, weeklyNotes) {
      var _a;
      return (_a = weeklyNotes[getDateUID(date, "week")]) != null ? _a : null;
    }
    function getAllWeeklyNotes() {
      const weeklyNotes = {};
      if (!appHasWeeklyNotesPluginLoaded()) {
        return weeklyNotes;
      }
      const { vault } = window.app;
      const { folder } = getWeeklyNoteSettings();
      const weeklyNotesFolder = vault.getAbstractFileByPath(obsidian.normalizePath(folder));
      if (!weeklyNotesFolder) {
        throw new WeeklyNotesFolderMissingError("Failed to find weekly notes folder");
      }
      obsidian.Vault.recurseChildren(weeklyNotesFolder, (note) => {
        if (note instanceof obsidian.TFile) {
          const date = getDateFromFile(note, "week");
          if (date) {
            const dateString = getDateUID(date, "week");
            weeklyNotes[dateString] = note;
          }
        }
      });
      return weeklyNotes;
    }
    var MonthlyNotesFolderMissingError = class extends Error {
    };
    async function createMonthlyNote(date) {
      const { vault } = window.app;
      const { template, format, folder } = getMonthlyNoteSettings();
      const [templateContents, IFoldInfo] = await getTemplateInfo(template);
      const filename = date.format(format);
      const normalizedPath = await getNotePath(folder, filename);
      try {
        const createdFile = await vault.create(normalizedPath, templateContents.replace(/{{\s*(date|time)\s*(([+-]\d+)([yqmwdhs]))?\s*(:.+?)?}}/gi, (_, _timeOrDate, calc, timeDelta, unit, momentFormat) => {
          const now = window.moment();
          const currentDate = date.clone().set({
            hour: now.get("hour"),
            minute: now.get("minute"),
            second: now.get("second")
          });
          if (calc) {
            currentDate.add(parseInt(timeDelta, 10), unit);
          }
          if (momentFormat) {
            return currentDate.format(momentFormat.substring(1).trim());
          }
          return currentDate.format(format);
        }).replace(/{{\s*date\s*}}/gi, filename).replace(/{{\s*time\s*}}/gi, window.moment().format("HH:mm")).replace(/{{\s*title\s*}}/gi, filename));
        window.app.foldManager.save(createdFile, IFoldInfo);
        return createdFile;
      } catch (err) {
        console.error(`Failed to create file: '${normalizedPath}'`, err);
        new obsidian.Notice("Unable to create new file.");
      }
    }
    function getMonthlyNote(date, monthlyNotes) {
      var _a;
      return (_a = monthlyNotes[getDateUID(date, "month")]) != null ? _a : null;
    }
    function getAllMonthlyNotes() {
      const monthlyNotes = {};
      if (!appHasMonthlyNotesPluginLoaded()) {
        return monthlyNotes;
      }
      const { vault } = window.app;
      const { folder } = getMonthlyNoteSettings();
      const monthlyNotesFolder = vault.getAbstractFileByPath(obsidian.normalizePath(folder));
      if (!monthlyNotesFolder) {
        throw new MonthlyNotesFolderMissingError("Failed to find monthly notes folder");
      }
      obsidian.Vault.recurseChildren(monthlyNotesFolder, (note) => {
        if (note instanceof obsidian.TFile) {
          const date = getDateFromFile(note, "month");
          if (date) {
            const dateString = getDateUID(date, "month");
            monthlyNotes[dateString] = note;
          }
        }
      });
      return monthlyNotes;
    }
    var QuarterlyNotesFolderMissingError = class extends Error {
    };
    async function createQuarterlyNote(date) {
      const { vault } = window.app;
      const { template, format, folder } = getQuarterlyNoteSettings();
      const [templateContents, IFoldInfo] = await getTemplateInfo(template);
      const filename = date.format(format);
      const normalizedPath = await getNotePath(folder, filename);
      try {
        const createdFile = await vault.create(normalizedPath, templateContents.replace(/{{\s*(date|time)\s*(([+-]\d+)([yqmwdhs]))?\s*(:.+?)?}}/gi, (_, _timeOrDate, calc, timeDelta, unit, momentFormat) => {
          const now = window.moment();
          const currentDate = date.clone().set({
            hour: now.get("hour"),
            minute: now.get("minute"),
            second: now.get("second")
          });
          if (calc) {
            currentDate.add(parseInt(timeDelta, 10), unit);
          }
          if (momentFormat) {
            return currentDate.format(momentFormat.substring(1).trim());
          }
          return currentDate.format(format);
        }).replace(/{{\s*date\s*}}/gi, filename).replace(/{{\s*time\s*}}/gi, window.moment().format("HH:mm")).replace(/{{\s*title\s*}}/gi, filename));
        window.app.foldManager.save(createdFile, IFoldInfo);
        return createdFile;
      } catch (err) {
        console.error(`Failed to create file: '${normalizedPath}'`, err);
        new obsidian.Notice("Unable to create new file.");
      }
    }
    function getQuarterlyNote(date, quarterly) {
      var _a;
      return (_a = quarterly[getDateUID(date, "quarter")]) != null ? _a : null;
    }
    function getAllQuarterlyNotes() {
      const quarterly = {};
      if (!appHasQuarterlyNotesPluginLoaded()) {
        return quarterly;
      }
      const { vault } = window.app;
      const { folder } = getQuarterlyNoteSettings();
      const quarterlyFolder = vault.getAbstractFileByPath(obsidian.normalizePath(folder));
      if (!quarterlyFolder) {
        throw new QuarterlyNotesFolderMissingError("Failed to find quarterly notes folder");
      }
      obsidian.Vault.recurseChildren(quarterlyFolder, (note) => {
        if (note instanceof obsidian.TFile) {
          const date = getDateFromFile(note, "quarter");
          if (date) {
            const dateString = getDateUID(date, "quarter");
            quarterly[dateString] = note;
          }
        }
      });
      return quarterly;
    }
    var YearlyNotesFolderMissingError = class extends Error {
    };
    async function createYearlyNote(date) {
      const { vault } = window.app;
      const { template, format, folder } = getYearlyNoteSettings();
      const [templateContents, IFoldInfo] = await getTemplateInfo(template);
      const filename = date.format(format);
      const normalizedPath = await getNotePath(folder, filename);
      try {
        const createdFile = await vault.create(normalizedPath, templateContents.replace(/{{\s*(date|time)\s*(([+-]\d+)([yqmwdhs]))?\s*(:.+?)?}}/gi, (_, _timeOrDate, calc, timeDelta, unit, momentFormat) => {
          const now = window.moment();
          const currentDate = date.clone().set({
            hour: now.get("hour"),
            minute: now.get("minute"),
            second: now.get("second")
          });
          if (calc) {
            currentDate.add(parseInt(timeDelta, 10), unit);
          }
          if (momentFormat) {
            return currentDate.format(momentFormat.substring(1).trim());
          }
          return currentDate.format(format);
        }).replace(/{{\s*date\s*}}/gi, filename).replace(/{{\s*time\s*}}/gi, window.moment().format("HH:mm")).replace(/{{\s*title\s*}}/gi, filename));
        window.app.foldManager.save(createdFile, IFoldInfo);
        return createdFile;
      } catch (err) {
        console.error(`Failed to create file: '${normalizedPath}'`, err);
        new obsidian.Notice("Unable to create new file.");
      }
    }
    function getYearlyNote(date, yearlyNotes) {
      var _a;
      return (_a = yearlyNotes[getDateUID(date, "year")]) != null ? _a : null;
    }
    function getAllYearlyNotes() {
      const yearlyNotes = {};
      if (!appHasYearlyNotesPluginLoaded()) {
        return yearlyNotes;
      }
      const { vault } = window.app;
      const { folder } = getYearlyNoteSettings();
      const yearlyNotesFolder = vault.getAbstractFileByPath(obsidian.normalizePath(folder));
      if (!yearlyNotesFolder) {
        throw new YearlyNotesFolderMissingError("Failed to find yearly notes folder");
      }
      obsidian.Vault.recurseChildren(yearlyNotesFolder, (note) => {
        if (note instanceof obsidian.TFile) {
          const date = getDateFromFile(note, "year");
          if (date) {
            const dateString = getDateUID(date, "year");
            yearlyNotes[dateString] = note;
          }
        }
      });
      return yearlyNotes;
    }
    function appHasDailyNotesPluginLoaded() {
      var _a, _b;
      const { app } = window;
      const dailyNotesPlugin = app.internalPlugins.plugins["daily-notes"];
      if (dailyNotesPlugin && dailyNotesPlugin.enabled) {
        return true;
      }
      const periodicNotes = app.plugins.getPlugin("periodic-notes");
      return periodicNotes && ((_b = (_a = periodicNotes.settings) == null ? void 0 : _a.daily) == null ? void 0 : _b.enabled);
    }
    function appHasWeeklyNotesPluginLoaded() {
      var _a, _b;
      const { app } = window;
      if (app.plugins.getPlugin("calendar")) {
        return true;
      }
      const periodicNotes = app.plugins.getPlugin("periodic-notes");
      return periodicNotes && ((_b = (_a = periodicNotes.settings) == null ? void 0 : _a.weekly) == null ? void 0 : _b.enabled);
    }
    function appHasMonthlyNotesPluginLoaded() {
      var _a, _b;
      const { app } = window;
      const periodicNotes = app.plugins.getPlugin("periodic-notes");
      return periodicNotes && ((_b = (_a = periodicNotes.settings) == null ? void 0 : _a.monthly) == null ? void 0 : _b.enabled);
    }
    function appHasQuarterlyNotesPluginLoaded() {
      var _a, _b;
      const { app } = window;
      const periodicNotes = app.plugins.getPlugin("periodic-notes");
      return periodicNotes && ((_b = (_a = periodicNotes.settings) == null ? void 0 : _a.quarterly) == null ? void 0 : _b.enabled);
    }
    function appHasYearlyNotesPluginLoaded() {
      var _a, _b;
      const { app } = window;
      const periodicNotes = app.plugins.getPlugin("periodic-notes");
      return periodicNotes && ((_b = (_a = periodicNotes.settings) == null ? void 0 : _a.yearly) == null ? void 0 : _b.enabled);
    }
    function getPeriodicNoteSettings(granularity) {
      const getSettings = {
        day: getDailyNoteSettings2,
        week: getWeeklyNoteSettings,
        month: getMonthlyNoteSettings,
        quarter: getQuarterlyNoteSettings,
        year: getYearlyNoteSettings
      }[granularity];
      return getSettings();
    }
    function createPeriodicNote(granularity, date) {
      const createFn = {
        day: createDailyNote,
        month: createMonthlyNote,
        week: createWeeklyNote
      };
      return createFn[granularity](date);
    }
    exports.DEFAULT_DAILY_NOTE_FORMAT = DEFAULT_DAILY_NOTE_FORMAT;
    exports.DEFAULT_MONTHLY_NOTE_FORMAT = DEFAULT_MONTHLY_NOTE_FORMAT;
    exports.DEFAULT_QUARTERLY_NOTE_FORMAT = DEFAULT_QUARTERLY_NOTE_FORMAT;
    exports.DEFAULT_WEEKLY_NOTE_FORMAT = DEFAULT_WEEKLY_NOTE_FORMAT;
    exports.DEFAULT_YEARLY_NOTE_FORMAT = DEFAULT_YEARLY_NOTE_FORMAT;
    exports.appHasDailyNotesPluginLoaded = appHasDailyNotesPluginLoaded;
    exports.appHasMonthlyNotesPluginLoaded = appHasMonthlyNotesPluginLoaded;
    exports.appHasQuarterlyNotesPluginLoaded = appHasQuarterlyNotesPluginLoaded;
    exports.appHasWeeklyNotesPluginLoaded = appHasWeeklyNotesPluginLoaded;
    exports.appHasYearlyNotesPluginLoaded = appHasYearlyNotesPluginLoaded;
    exports.createDailyNote = createDailyNote;
    exports.createMonthlyNote = createMonthlyNote;
    exports.createPeriodicNote = createPeriodicNote;
    exports.createQuarterlyNote = createQuarterlyNote;
    exports.createWeeklyNote = createWeeklyNote;
    exports.createYearlyNote = createYearlyNote;
    exports.getAllDailyNotes = getAllDailyNotes;
    exports.getAllMonthlyNotes = getAllMonthlyNotes;
    exports.getAllQuarterlyNotes = getAllQuarterlyNotes;
    exports.getAllWeeklyNotes = getAllWeeklyNotes;
    exports.getAllYearlyNotes = getAllYearlyNotes;
    exports.getDailyNote = getDailyNote;
    exports.getDailyNoteSettings = getDailyNoteSettings2;
    exports.getDateFromFile = getDateFromFile;
    exports.getDateFromPath = getDateFromPath;
    exports.getDateUID = getDateUID;
    exports.getMonthlyNote = getMonthlyNote;
    exports.getMonthlyNoteSettings = getMonthlyNoteSettings;
    exports.getPeriodicNoteSettings = getPeriodicNoteSettings;
    exports.getQuarterlyNote = getQuarterlyNote;
    exports.getQuarterlyNoteSettings = getQuarterlyNoteSettings;
    exports.getTemplateInfo = getTemplateInfo;
    exports.getWeeklyNote = getWeeklyNote;
    exports.getWeeklyNoteSettings = getWeeklyNoteSettings;
    exports.getYearlyNote = getYearlyNote;
    exports.getYearlyNoteSettings = getYearlyNoteSettings;
  }
});

// src/main.ts
var main_exports = {};
__export(main_exports, {
  default: () => ThePlugin
});
module.exports = __toCommonJS(main_exports);
var import_obsidian11 = require("obsidian");

// src/ui/SettingsTab.ts
var import_obsidian5 = require("obsidian");

// src/features/themes.ts
var import_obsidian3 = require("obsidian");

// src/features/githubUtils.ts
var import_obsidian = require("obsidian");
var GITHUB_RAW_USERCONTENT_PATH = "https://raw.githubusercontent.com/";
var grabReleaseFileFromRepository = async (repository, version, fileName, debugLogging = true) => {
  const URL = `https://github.com/${repository}/releases/download/${version}/${fileName}`;
  try {
    const download = await (0, import_obsidian.request)({ url: URL });
    return download === "Not Found" || download === `{"error":"Not Found"}` ? null : download;
  } catch (error) {
    if (debugLogging)
      console.log("error in grabReleaseFileFromRepository", URL, error);
    return null;
  }
};
var grabManifestJsonFromRepository = async (repositoryPath, rootManifest = true, debugLogging = true) => {
  const manifestJsonPath = GITHUB_RAW_USERCONTENT_PATH + repositoryPath + (rootManifest === true ? "/HEAD/manifest.json" : "/HEAD/manifest-beta.json");
  try {
    const response = await (0, import_obsidian.request)({ url: manifestJsonPath });
    return response === "404: Not Found" ? null : await JSON.parse(response);
  } catch (error) {
    if (error != "Error: Request failed, status 404" && debugLogging) {
      console.log(`error in grabManifestJsonFromRepository for ${manifestJsonPath}`, error);
    }
    return null;
  }
};
var grabCommmunityPluginList = async (debugLogging = true) => {
  const pluginListURL = `https://raw.githubusercontent.com/obsidianmd/obsidian-releases/HEAD/community-plugins.json`;
  try {
    const response = await (0, import_obsidian.request)({ url: pluginListURL });
    return response === "404: Not Found" ? null : await JSON.parse(response);
  } catch (error) {
    if (debugLogging)
      console.log("error in grabCommmunityPluginList", error);
    return null;
  }
};
var grabCommmunityThemesList = async (debugLogging = true) => {
  const themesURL = `https://raw.githubusercontent.com/obsidianmd/obsidian-releases/HEAD/community-css-themes.json`;
  try {
    const response = await (0, import_obsidian.request)({ url: themesURL });
    return response === "404: Not Found" ? null : await JSON.parse(response);
  } catch (error) {
    if (debugLogging)
      console.log("error in grabCommmunityThemesList", error);
    return null;
  }
};
var grabCommmunityThemeCssFile = async (repositoryPath, betaVersion = false, debugLogging) => {
  const themesURL = `https://raw.githubusercontent.com/${repositoryPath}/HEAD/theme${betaVersion ? "-beta" : ""}.css`;
  try {
    const response = await (0, import_obsidian.request)({ url: themesURL });
    return response === "404: Not Found" ? null : response;
  } catch (error) {
    if (debugLogging)
      console.log("error in grabCommmunityThemeCssFile", error);
    return null;
  }
};
var grabCommmunityThemeManifestFile = async (repositoryPath, debugLogging = true) => {
  const themesURL = `https://raw.githubusercontent.com/${repositoryPath}/HEAD/manifest.json`;
  try {
    const response = await (0, import_obsidian.request)({ url: themesURL });
    return response === "404: Not Found" ? null : response;
  } catch (error) {
    if (debugLogging)
      console.log("error in grabCommmunityThemeManifestFile", error);
    return null;
  }
};
var checksum = (str) => {
  let sum = 0;
  for (let i = 0; i < str.length; i++) {
    sum += str.charCodeAt(i);
  }
  return sum;
};
var checksumForString = (str) => {
  return checksum(str).toString();
};
var grabChecksumOfThemeCssFile = async (repositoryPath, betaVersion, debugLogging) => {
  const themeCSS = await grabCommmunityThemeCssFile(repositoryPath, betaVersion, debugLogging);
  return themeCSS ? checksumForString(themeCSS) : "0";
};
var grabLastCommitInfoForAFile = async (repositoryPath, path, debugLogging = true) => {
  const url = `https://api.github.com/repos/${repositoryPath}/commits?path=${path}&page=1&per_page=1`;
  try {
    const response = await (0, import_obsidian.request)({ url });
    return response === "404: Not Found" ? null : JSON.parse(response);
  } catch (error) {
    if (debugLogging)
      console.log("error in grabLastCommitInfoForAFile", error);
    return null;
  }
};
var grabLastCommitDateForAFile = async (repositoryPath, path) => {
  const test = await grabLastCommitInfoForAFile(repositoryPath, path);
  if (test[0].commit.committer.date) {
    return test[0].commit.committer.date;
  } else
    return "";
};

// src/ui/settings.ts
var DEFAULT_SETTINGS = {
  pluginList: [],
  pluginSubListFrozenVersion: [],
  themesList: [],
  updateAtStartup: false,
  updateThemesAtStartup: false,
  ribbonIconEnabled: true,
  loggingEnabled: false,
  loggingPath: "BRAT-log",
  loggingVerboseEnabled: false,
  debuggingMode: true,
  notificationsEnabled: true
};
async function addBetaPluginToList(plugin, repositoryPath, specifyVersion = "") {
  let save = false;
  if (!plugin.settings.pluginList.contains(repositoryPath)) {
    plugin.settings.pluginList.unshift(repositoryPath);
    save = true;
  }
  if (specifyVersion !== "" && plugin.settings.pluginSubListFrozenVersion.filter((x) => x.repo === repositoryPath).length === 0) {
    plugin.settings.pluginSubListFrozenVersion.unshift({
      repo: repositoryPath,
      version: specifyVersion
    });
    save = true;
  }
  if (save) {
    plugin.saveSettings();
  }
}
async function existBetaPluginInList(plugin, repositoryPath) {
  return plugin.settings.pluginList.contains(repositoryPath);
}
async function addBetaThemeToList(plugin, repositoryPath, themeCSS) {
  const newTheme = {
    repo: repositoryPath,
    lastUpdate: checksumForString(themeCSS)
  };
  plugin.settings.themesList.unshift(newTheme);
  plugin.saveSettings();
}
async function existBetaThemeinInList(plugin, repositoryPath) {
  const testIfThemExists = plugin.settings.themesList.find((t) => t.repo === repositoryPath);
  return testIfThemExists ? true : false;
}
function updateBetaThemeLastUpdateChecksum(plugin, repositoryPath, checksum2) {
  plugin.settings.themesList.forEach((t) => {
    if (t.repo === repositoryPath) {
      t.lastUpdate = checksum2;
      plugin.saveSettings();
    }
  });
}

// src/utils/notifications.ts
var import_obsidian2 = require("obsidian");
function ToastMessage(plugin, msg, timeoutInSeconds = 10, contextMenuCallback) {
  if (plugin.settings.notificationsEnabled === false)
    return;
  const additionalInfo = contextMenuCallback ? import_obsidian2.Platform.isDesktop ? "(click=dismiss, right-click=Info)" : "(click=dismiss)" : "";
  const newNotice = new import_obsidian2.Notice(`BRAT
${msg}
${additionalInfo}`, timeoutInSeconds * 1e3);
  if (contextMenuCallback)
    newNotice.noticeEl.oncontextmenu = async () => {
      contextMenuCallback();
    };
}

// src/utils/internetconnection.ts
async function isConnectedToInternet() {
  try {
    const online = await fetch("https://obsidian.md/?" + Math.random());
    return online.status >= 200 && online.status < 300;
  } catch (err) {
    return false;
  }
}

// src/features/themes.ts
var themeSave = async (plugin, cssGithubRepository, newInstall) => {
  let themeCSS = await grabCommmunityThemeCssFile(cssGithubRepository, true, plugin.settings.debuggingMode);
  if (!themeCSS)
    themeCSS = await grabCommmunityThemeCssFile(cssGithubRepository, false, plugin.settings.debuggingMode);
  if (!themeCSS) {
    ToastMessage(plugin, "There is no theme.css or theme-beta.css file in the root path of this repository, so there is no theme to install.");
    return false;
  }
  const themeManifest = await grabCommmunityThemeManifestFile(cssGithubRepository, plugin.settings.debuggingMode);
  if (!themeManifest) {
    ToastMessage(plugin, "There is no manifest.json file in the root path of this repository, so theme cannot be installed.");
    return false;
  }
  const manifestInfo = await JSON.parse(themeManifest);
  const themeTargetFolderPath = (0, import_obsidian3.normalizePath)(themesRootPath(plugin) + manifestInfo.name);
  const adapter = plugin.app.vault.adapter;
  if (await adapter.exists(themeTargetFolderPath) === false)
    await adapter.mkdir(themeTargetFolderPath);
  await adapter.write((0, import_obsidian3.normalizePath)(themeTargetFolderPath + "/theme.css"), themeCSS);
  await adapter.write((0, import_obsidian3.normalizePath)(themeTargetFolderPath + "/manifest.json"), themeManifest);
  updateBetaThemeLastUpdateChecksum(plugin, cssGithubRepository, checksumForString(themeCSS));
  let msg = ``;
  if (newInstall) {
    await addBetaThemeToList(plugin, cssGithubRepository, themeCSS);
    msg = `${manifestInfo.name} theme installed from ${cssGithubRepository}. `;
    setTimeout(() => {
      plugin.app.customCss.setTheme(manifestInfo.name);
    }, 500);
  } else {
    msg = `${manifestInfo.name} theme updated from ${cssGithubRepository}.`;
  }
  plugin.log(msg + `[Theme Info](https://github.com/${cssGithubRepository})`, false);
  ToastMessage(plugin, `${msg}`, 20, async () => {
    window.open(`https://github.com/${cssGithubRepository}`);
  });
  return true;
};
var themesCheckAndUpdates = async (plugin, showInfo) => {
  if (await isConnectedToInternet() === false) {
    console.log("BRAT: No internet detected.");
    return;
  }
  let newNotice;
  const msg1 = `Checking for beta theme updates STARTED`;
  plugin.log(msg1, true);
  if (showInfo && plugin.settings.notificationsEnabled)
    newNotice = new import_obsidian3.Notice(`BRAT
${msg1}`, 3e4);
  for (const t of plugin.settings.themesList) {
    let lastUpdateOnline = await grabChecksumOfThemeCssFile(t.repo, true, plugin.settings.debuggingMode);
    if (lastUpdateOnline === "0")
      lastUpdateOnline = await grabChecksumOfThemeCssFile(t.repo, false, plugin.settings.debuggingMode);
    if (lastUpdateOnline !== t.lastUpdate)
      await themeSave(plugin, t.repo, false);
  }
  const msg2 = `Checking for beta theme updates COMPLETED`;
  plugin.log(msg2, true);
  if (showInfo) {
    if (plugin.settings.notificationsEnabled)
      newNotice.hide();
    ToastMessage(plugin, msg2);
  }
};
var themeDelete = async (plugin, cssGithubRepository) => {
  plugin.settings.themesList = plugin.settings.themesList.filter((t) => t.repo != cssGithubRepository);
  plugin.saveSettings();
  const msg = `Removed ${cssGithubRepository} from BRAT themes list and will no longer be updated. However, the theme files still exist in the vault. To remove them, go into Settings > Appearance and remove the theme.`;
  plugin.log(msg, true);
  ToastMessage(plugin, `${msg}`);
};
var themesRootPath = (plugin) => {
  return (0, import_obsidian3.normalizePath)(plugin.app.vault.configDir + "/themes") + "/";
};

// src/ui/AddNewTheme.ts
var import_obsidian4 = require("obsidian");

// src/ui/Promotional.ts
var promotionalLinks = (containerEl, settingsTab = true) => {
  const linksDiv = containerEl.createEl("div");
  linksDiv.style.float = "right";
  if (settingsTab === false) {
    linksDiv.style.padding = "10px";
    linksDiv.style.paddingLeft = "15px";
    linksDiv.style.paddingRight = "15px";
  } else {
    linksDiv.style.padding = "15px";
    linksDiv.style.paddingLeft = "15px";
    linksDiv.style.paddingRight = "15px";
    linksDiv.style.marginLeft = "15px";
  }
  const twitterSpan = linksDiv.createDiv("coffee");
  twitterSpan.addClass("ex-twitter-span");
  twitterSpan.style.paddingLeft = "10px";
  const captionText = twitterSpan.createDiv();
  captionText.innerText = "Learn more about my work at:";
  twitterSpan.appendChild(captionText);
  const twitterLink = twitterSpan.createEl("a", { href: "https://tfthacker.com" });
  twitterLink.innerText = "https://tfthacker.com";
  return linksDiv;
};

// src/ui/AddNewTheme.ts
var AddNewTheme = class extends import_obsidian4.Modal {
  constructor(plugin, openSettingsTabAfterwards = false) {
    super(plugin.app);
    this.plugin = plugin;
    this.address = "";
    this.openSettingsTabAfterwards = openSettingsTabAfterwards;
  }
  async submitForm() {
    if (this.address === "")
      return;
    const scrubbedAddress = this.address.replace("https://github.com/", "");
    if (await existBetaThemeinInList(this.plugin, scrubbedAddress)) {
      ToastMessage(this.plugin, `This plugin is already in the list for beta testing`, 10);
      return;
    }
    if (await themeSave(this.plugin, scrubbedAddress, true)) {
      this.close();
    }
  }
  onOpen() {
    this.contentEl.createEl("h4", { text: "Github repository for beta theme:" });
    this.contentEl.createEl("form", {}, (formEl) => {
      formEl.addClass("brat-modal");
      new import_obsidian4.Setting(formEl).addText((textEl) => {
        textEl.setPlaceholder("Repository (example: https://github.com/GitubUserName/repository-name");
        textEl.onChange((value) => {
          this.address = value.trim();
        });
        textEl.inputEl.addEventListener("keydown", async (e) => {
          if (e.key === "Enter" && this.address !== " ") {
            e.preventDefault();
            await this.submitForm();
          }
        });
        textEl.inputEl.style.width = "100%";
        window.setTimeout(() => {
          const title = document.querySelector(".setting-item-info");
          if (title)
            title.remove();
          textEl.inputEl.focus();
        }, 10);
      });
      formEl.createDiv("modal-button-container", (buttonContainerEl) => {
        buttonContainerEl.createEl("button", { attr: { type: "button" }, text: "Never mind" }).addEventListener("click", () => this.close());
        buttonContainerEl.createEl("button", {
          attr: { type: "submit" },
          cls: "mod-cta",
          text: "Add Theme"
        });
      });
      const newDiv = formEl.createDiv();
      newDiv.style.borderTop = "1px solid #ccc";
      newDiv.style.marginTop = "30px";
      const byTfThacker = newDiv.createSpan();
      byTfThacker.innerHTML = "BRAT by <a href='https://bit.ly/o42-twitter'>TFTHacker</a>";
      byTfThacker.style.fontStyle = "italic";
      newDiv.appendChild(byTfThacker);
      promotionalLinks(newDiv, false);
      window.setTimeout(() => {
        const title = formEl.querySelectorAll(".brat-modal .setting-item-info");
        title.forEach((titleEl) => {
          titleEl.remove();
        });
      }, 50);
      formEl.addEventListener("submit", async (e) => {
        e.preventDefault();
        if (this.address !== "")
          await this.submitForm();
      });
    });
  }
  async onClose() {
    if (this.openSettingsTabAfterwards) {
      await this.plugin.app.setting.open();
      await this.plugin.app.setting.openTabById("obsidian42-brat");
    }
  }
};

// src/ui/SettingsTab.ts
var BratSettingsTab = class extends import_obsidian5.PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }
  display() {
    const { containerEl } = this;
    containerEl.empty();
    promotionalLinks(containerEl, true);
    containerEl.createEl("h1", { text: this.plugin.appName });
    containerEl.createEl("h2", { text: "by TfTHacker" });
    new import_obsidian5.Setting(containerEl).setName("Auto-update plugins at startup").setDesc("If enabled all beta plugins will be checked for updates each time Obsidian starts. Note: this does not update frozen version plugins.").addToggle((cb) => {
      cb.setValue(this.plugin.settings.updateAtStartup);
      cb.onChange(async (value) => {
        this.plugin.settings.updateAtStartup = value;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian5.Setting(containerEl).setName("Auto-update themes at startup").setDesc("If enabled all beta themes will be checked for updates each time Obsidian starts.").addToggle((cb) => {
      cb.setValue(this.plugin.settings.updateThemesAtStartup);
      cb.onChange(async (value) => {
        this.plugin.settings.updateThemesAtStartup = value;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian5.Setting(containerEl).setName("Ribbon Button").setDesc("Toggle ribbon button off and on.").addToggle((cb) => {
      cb.setValue(this.plugin.settings.ribbonIconEnabled);
      cb.onChange(async (value) => {
        this.plugin.settings.ribbonIconEnabled = value;
        if (this.plugin.settings.ribbonIconEnabled === false)
          this.plugin.ribbonIcon.remove();
        else
          this.plugin.showRibbonButton();
        await this.plugin.saveSettings();
      });
    });
    containerEl.createEl("hr");
    containerEl.createEl("h2", { text: "Beta Plugin List" });
    containerEl.createEl("div", { text: `The following is a list of beta plugins added via the command palette "Add a beta plugin for testing" or "Add a beta plugin with frozen version for testing". A frozen version is a specific release of a plugin based on its releease tag. ` });
    containerEl.createEl("p");
    containerEl.createEl("div", { text: `Click the x button next to a plugin to remove it from the list.` });
    containerEl.createEl("p");
    containerEl.createEl("span").createEl("b", { text: "Note: " });
    containerEl.createSpan({ text: "This does not delete the plugin, this should be done from the  Community Plugins tab in Settings." });
    new import_obsidian5.Setting(containerEl).addButton((cb) => {
      cb.setButtonText("Add Beta plugin");
      cb.onClick(async () => {
        this.plugin.app.setting.close();
        await this.plugin.betaPlugins.displayAddNewPluginModal(true, false);
      });
    });
    const pluginSubListFrozenVersionNames = new Set(this.plugin.settings.pluginSubListFrozenVersion.map((x) => x.repo));
    for (const bp of this.plugin.settings.pluginList) {
      if (pluginSubListFrozenVersionNames.has(bp)) {
        continue;
      }
      new import_obsidian5.Setting(containerEl).setName(bp).addButton((btn) => {
        btn.setIcon("cross");
        btn.setTooltip("Delete this beta plugin");
        btn.onClick(async () => {
          if (btn.buttonEl.textContent === "")
            btn.setButtonText("Click once more to confirm removal");
          else {
            btn.buttonEl.parentElement.parentElement.remove();
            await this.plugin.betaPlugins.deletePlugin(bp);
          }
        });
      });
    }
    new import_obsidian5.Setting(containerEl).addButton((cb) => {
      cb.setButtonText("Add Beta plugin with frozen version");
      cb.onClick(async () => {
        this.plugin.app.setting.close();
        await this.plugin.betaPlugins.displayAddNewPluginModal(true, true);
      });
    });
    for (const bp of this.plugin.settings.pluginSubListFrozenVersion) {
      new import_obsidian5.Setting(containerEl).setName(`${bp.repo} (version ${bp.version})`).addButton((btn) => {
        btn.setIcon("cross");
        btn.setTooltip("Delete this beta plugin");
        btn.onClick(async () => {
          if (btn.buttonEl.textContent === "")
            btn.setButtonText("Click once more to confirm removal");
          else {
            btn.buttonEl.parentElement.parentElement.remove();
            await this.plugin.betaPlugins.deletePlugin(bp.repo);
          }
        });
      });
    }
    containerEl.createEl("hr");
    containerEl.createEl("h2", { text: "Beta Themes List" });
    new import_obsidian5.Setting(containerEl).addButton((cb) => {
      cb.setButtonText("Add Beta Theme");
      cb.onClick(async () => {
        this.plugin.app.setting.close();
        new AddNewTheme(this.plugin).open();
      });
    });
    for (const bp of this.plugin.settings.themesList) {
      new import_obsidian5.Setting(containerEl).setName(bp.repo).addButton((btn) => {
        btn.setIcon("cross");
        btn.setTooltip("Delete this beta theme");
        btn.onClick(async () => {
          if (btn.buttonEl.textContent === "")
            btn.setButtonText("Click once more to confirm removal");
          else {
            btn.buttonEl.parentElement.parentElement.remove();
            await themeDelete(this.plugin, bp.repo);
          }
        });
      });
    }
    containerEl.createEl("hr");
    containerEl.createEl("h2", { text: "Monitoring" });
    new import_obsidian5.Setting(containerEl).setName("Enable Notifications").setDesc("BRAT will provide popup notifications for its various activities. Turn this off means  no notifications from BRAT.").addToggle((cb) => {
      cb.setValue(this.plugin.settings.notificationsEnabled);
      cb.onChange(async (value) => {
        this.plugin.settings.notificationsEnabled = value;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian5.Setting(containerEl).setName("Enable Logging").setDesc("Plugin updates will be logged to a file in the log file.").addToggle((cb) => {
      cb.setValue(this.plugin.settings.loggingEnabled);
      cb.onChange(async (value) => {
        this.plugin.settings.loggingEnabled = value;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian5.Setting(this.containerEl).setName("BRAT Log File Location").setDesc("Logs will be saved to this file. Don't add .md to the file name.").addSearch((cb) => {
      cb.setPlaceholder("Example: BRAT-log").setValue(this.plugin.settings.loggingPath).onChange(async (new_folder) => {
        this.plugin.settings.loggingPath = new_folder;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian5.Setting(containerEl).setName("Enable Verbose Logging").setDesc("Get a lot  more information in  the log.").addToggle((cb) => {
      cb.setValue(this.plugin.settings.loggingVerboseEnabled);
      cb.onChange(async (value) => {
        this.plugin.settings.loggingVerboseEnabled = value;
        await this.plugin.saveSettings();
      });
    });
    new import_obsidian5.Setting(containerEl).setName("Debugging Mode").setDesc("Atomic Bomb level console logging. Can be used for troubleshoting and development.").addToggle((cb) => {
      cb.setValue(this.plugin.settings.debuggingMode);
      cb.onChange(async (value) => {
        this.plugin.settings.debuggingMode = value;
        await this.plugin.saveSettings();
      });
    });
  }
};

// src/ui/AddNewPluginModal.ts
var import_obsidian6 = require("obsidian");
var AddNewPluginModal = class extends import_obsidian6.Modal {
  constructor(plugin, betaPlugins, openSettingsTabAfterwards = false, useFrozenVersion = false) {
    super(plugin.app);
    this.plugin = plugin;
    this.betaPlugins = betaPlugins;
    this.address = "";
    this.openSettingsTabAfterwards = openSettingsTabAfterwards;
    this.useFrozenVersion = useFrozenVersion;
    this.version = "";
  }
  async submitForm() {
    if (this.address === "")
      return;
    let scrubbedAddress = this.address.replace("https://github.com/", "");
    if (scrubbedAddress.endsWith(".git"))
      scrubbedAddress = scrubbedAddress.slice(0, -4);
    if (await existBetaPluginInList(this.plugin, scrubbedAddress)) {
      ToastMessage(this.plugin, `This plugin is already in the list for beta testing`, 10);
      return;
    }
    const result = await this.betaPlugins.addPlugin(scrubbedAddress, false, false, false, this.version);
    if (result) {
      this.close();
    }
  }
  onOpen() {
    this.contentEl.createEl("h4", { text: "Github repository for beta plugin:" });
    this.contentEl.createEl("form", {}, (formEl) => {
      formEl.addClass("brat-modal");
      new import_obsidian6.Setting(formEl).addText((textEl) => {
        textEl.setPlaceholder("Repository (example: https://github.com/GitubUserName/repository-name)");
        textEl.onChange((value) => {
          this.address = value.trim();
        });
        textEl.inputEl.addEventListener("keydown", async (e) => {
          if (e.key === "Enter" && this.address !== " ") {
            if (this.useFrozenVersion && this.version !== "" || !this.useFrozenVersion) {
              e.preventDefault();
              await this.submitForm();
            }
          }
        });
        textEl.inputEl.style.width = "100%";
      });
      if (this.useFrozenVersion) {
        new import_obsidian6.Setting(formEl).addText((textEl) => {
          textEl.setPlaceholder("Specify the release version tag (example: 1.0.0)");
          textEl.onChange((value) => {
            this.version = value.trim();
          });
          textEl.inputEl.style.width = "100%";
        });
      }
      formEl.createDiv("modal-button-container", (buttonContainerEl) => {
        buttonContainerEl.createEl("button", { attr: { type: "button" }, text: "Never mind" }).addEventListener("click", () => this.close());
        buttonContainerEl.createEl("button", {
          attr: { type: "submit" },
          cls: "mod-cta",
          text: "Add Plugin"
        });
      });
      const newDiv = formEl.createDiv();
      newDiv.style.borderTop = "1px solid #ccc";
      newDiv.style.marginTop = "30px";
      const byTfThacker = newDiv.createSpan();
      byTfThacker.innerHTML = "BRAT by <a href='https://bit.ly/o42-twitter'>TFTHacker</a>";
      byTfThacker.style.fontStyle = "italic";
      newDiv.appendChild(byTfThacker);
      promotionalLinks(newDiv, false);
      window.setTimeout(() => {
        const title = formEl.querySelectorAll(".brat-modal .setting-item-info");
        title.forEach((titleEl) => {
          titleEl.remove();
        });
      }, 50);
      formEl.addEventListener("submit", async (e) => {
        e.preventDefault();
        if (this.address !== "") {
          if (this.useFrozenVersion && this.version !== "" || !this.useFrozenVersion) {
            await this.submitForm();
          }
        }
      });
    });
  }
  async onClose() {
    if (this.openSettingsTabAfterwards) {
      await this.plugin.app.setting.open();
      await this.plugin.app.setting.openTabById("obsidian42-brat");
    }
  }
};

// src/features/BetaPlugins.ts
var import_obsidian7 = require("obsidian");
var BetaPlugins = class {
  constructor(plugin) {
    this.plugin = plugin;
  }
  /**
   * opens the AddNewPluginModal to get info for  a new beta plugin
   * @param   {boolean}   openSettingsTabAfterwards will open settings screen afterwards. Used when this command is called from settings tab
   * @param   {boolean}   useFrozenVersion          install the plugin using frozen version.
   * @return  {<Promise><void>}
   */
  async displayAddNewPluginModal(openSettingsTabAfterwards = false, useFrozenVersion = false) {
    const newPlugin = new AddNewPluginModal(this.plugin, this, openSettingsTabAfterwards, useFrozenVersion);
    newPlugin.open();
  }
  /**
   * Validates that a GitHub repository is plugin
   *
   * @param   {string}                     repositoryPath   GithubUser/RepositoryName (example: TfThacker/obsidian42-brat)
   * @param   {[type]}                     getBetaManifest  test the beta version of the manifest, not at the root
   * @param   {[type]}                     false            [false description]
   * @param   {[type]}                     reportIssues      will display notices as it finds issues
   *
   * @return  {Promise<PluginManifest>}                     the manifest file if found, or null if its incomplete
   */
  async validateRepository(repositoryPath, getBetaManifest = false, reportIssues = false) {
    const noticeTimeout = 15;
    const manifestJson = await grabManifestJsonFromRepository(repositoryPath, !getBetaManifest, this.plugin.settings.debuggingMode);
    if (!manifestJson) {
      if (reportIssues)
        ToastMessage(this.plugin, `${repositoryPath}
This does not seem to be an obsidian plugin, as there is no manifest.json file.`, noticeTimeout);
      return null;
    }
    if (!("id" in manifestJson)) {
      if (reportIssues)
        ToastMessage(this.plugin, `${repositoryPath}
The plugin id attribute for the release is missing from the manifest file`, noticeTimeout);
      return null;
    }
    if (!("version" in manifestJson)) {
      if (reportIssues)
        ToastMessage(this.plugin, `${repositoryPath}
The version attribute for the release is missing from the manifest file`, noticeTimeout);
      return null;
    }
    return manifestJson;
  }
  /**
   * Gets all the release files based on the version number in the manifest
   *
   * @param   {string}                        repositoryPath  path to the GitHub repository
   * @param   {PluginManifest<ReleaseFiles>}  manifest        manifest file
   * @param   {boolean}                       getManifest     grab the remote manifest file
   * @param   {string}                        specifyVersion  grab the specified version if set
   *
   * @return  {Promise<ReleaseFiles>}                         all relase files as strings based on the ReleaseFiles interaface
   */
  async getAllReleaseFiles(repositoryPath, manifest, getManifest, specifyVersion = "") {
    const version = specifyVersion === "" ? manifest.version : specifyVersion;
    const reallyGetManifestOrNot = getManifest || specifyVersion !== "";
    return {
      mainJs: await grabReleaseFileFromRepository(repositoryPath, version, "main.js", this.plugin.settings.debuggingMode),
      manifest: reallyGetManifestOrNot ? await grabReleaseFileFromRepository(repositoryPath, version, "manifest.json", this.plugin.settings.debuggingMode) : "",
      styles: await grabReleaseFileFromRepository(repositoryPath, version, "styles.css", this.plugin.settings.debuggingMode)
    };
  }
  /**
   * Writes the plugin release files to the local obsidian .plugins folder
   *
   * @param   {string}              betaPluginID  the id of the plugin (not the repository path)
   * @param   {ReleaseFiles<void>}  relFiles      release file as strings, based on the ReleaseFiles interface
   *
   * @return  {Promise<void>}                     
   */
  async writeReleaseFilesToPluginFolder(betaPluginID, relFiles) {
    const pluginTargetFolderPath = (0, import_obsidian7.normalizePath)(this.plugin.app.vault.configDir + "/plugins/" + betaPluginID) + "/";
    const adapter = this.plugin.app.vault.adapter;
    if (await adapter.exists(pluginTargetFolderPath) === false || !await adapter.exists(pluginTargetFolderPath + "manifest.json")) {
      await adapter.mkdir(pluginTargetFolderPath);
    }
    await adapter.write(pluginTargetFolderPath + "main.js", relFiles.mainJs);
    await adapter.write(pluginTargetFolderPath + "manifest.json", relFiles.manifest);
    if (relFiles.styles)
      await adapter.write(pluginTargetFolderPath + "styles.css", relFiles.styles);
  }
  /**
   * Primary function for adding a new beta plugin to Obsidian. 
   * Also this function is used for updating existing plugins.
   *
   * @param   {string}              repositoryPath     path to GitHub repository formated as USERNAME/repository
   * @param   {boolean}             updatePluginFiles  true if this is just an update not an install
   * @param   {boolean}             seeIfUpdatedOnly   if true, and updatePluginFiles true, will just check for updates, but not do the update. will report to user that there is a new plugin
   * @param   {boolean}             reportIfNotUpdted  if true, report if an update has not succed
   * @param   {string}              specifyVersion     if not empty, need to install a specified version instead of the value in manifest{-beta}.json
   * @param   {boolean}             forceReinstall     if true, will force a reinstall of the plugin, even if it is already installed
   *
   * @return  {Promise<boolean>}                       true if succeeds
   */
  async addPlugin(repositoryPath, updatePluginFiles = false, seeIfUpdatedOnly = false, reportIfNotUpdted = false, specifyVersion = "", forceReinstall = false) {
    var _a;
    const noticeTimeout = 10;
    let primaryManifest = await this.validateRepository(repositoryPath, true, false);
    const usingBetaManifest = primaryManifest ? true : false;
    if (usingBetaManifest === false)
      primaryManifest = await this.validateRepository(repositoryPath, false, true);
    if (primaryManifest === null) {
      const msg = `${repositoryPath}
A manifest.json or manifest-beta.json file does not exist in the root directory of the repository. This plugin cannot be installed.`;
      this.plugin.log(msg, true);
      ToastMessage(this.plugin, `${msg}`, noticeTimeout);
      return false;
    }
    if (!primaryManifest.hasOwnProperty("version")) {
      const msg = `${repositoryPath}
The manifest${usingBetaManifest ? "-beta" : ""}.json file in the root directory of the repository does not have a version number in the file. This plugin cannot be installed.`;
      this.plugin.log(msg, true);
      ToastMessage(this.plugin, `${msg}`, noticeTimeout);
      return false;
    }
    if (primaryManifest.hasOwnProperty("minAppVersion")) {
      if (!(0, import_obsidian7.requireApiVersion)(primaryManifest.minAppVersion)) {
        const msg = `Plugin: ${repositoryPath}

The manifest${usingBetaManifest ? "-beta" : ""}.json for this plugin indicates that the Obsidian version of the app needs to be ${primaryManifest.minAppVersion}, but this installation of Obsidian is ${import_obsidian7.apiVersion}. 

You will need to update your Obsidian to use this plugin or contact the plugin developer for more information.`;
        this.plugin.log(msg, true);
        ToastMessage(this.plugin, `${msg}`, 30);
        return false;
      }
    }
    const getRelease = async () => {
      const rFiles = await this.getAllReleaseFiles(repositoryPath, primaryManifest, usingBetaManifest, specifyVersion);
      if (usingBetaManifest || rFiles.manifest === "")
        rFiles.manifest = JSON.stringify(primaryManifest);
      if (rFiles.mainJs === null) {
        const msg = `${repositoryPath}
The release is not complete and cannot be download. main.js is missing from the Release`;
        this.plugin.log(msg, true);
        ToastMessage(this.plugin, `${msg}`, noticeTimeout);
        return null;
      }
      return rFiles;
    };
    if (updatePluginFiles === false || forceReinstall === true) {
      const releaseFiles = await getRelease();
      if (releaseFiles === null)
        return false;
      await this.writeReleaseFilesToPluginFolder(primaryManifest.id, releaseFiles);
      if (forceReinstall === false)
        await addBetaPluginToList(this.plugin, repositoryPath, specifyVersion);
      await this.plugin.app.plugins.loadManifests();
      if (forceReinstall === true) {
        await this.reloadPlugin(primaryManifest.id);
        this.plugin.log(`${repositoryPath} reinstalled`, true);
        ToastMessage(this.plugin, `${repositoryPath}
Plugin has been reinstalled and reloaded.`, noticeTimeout);
      } else {
        const versionText = specifyVersion === "" ? "" : ` (version: ${specifyVersion})`;
        const msg = `${repositoryPath}${versionText}
The plugin has been registered with BRAT. You may still need to enable it the Community Plugin List.`;
        this.plugin.log(msg, true);
        ToastMessage(this.plugin, msg, noticeTimeout);
      }
    } else {
      const pluginTargetFolderPath = this.plugin.app.vault.configDir + "/plugins/" + primaryManifest.id + "/";
      let localManifestContents = "";
      try {
        localManifestContents = await this.plugin.app.vault.adapter.read(pluginTargetFolderPath + "manifest.json");
      } catch (e) {
        if (e.errno === -4058 || e.errno === -2) {
          await this.addPlugin(repositoryPath, false, usingBetaManifest, false, specifyVersion);
          return true;
        } else
          console.log("BRAT - Local Manifest Load", primaryManifest.id, JSON.stringify(e, null, 2));
      }
      if (specifyVersion !== "" || this.plugin.settings.pluginSubListFrozenVersion.map((x) => x.repo).includes(repositoryPath)) {
        ToastMessage(this.plugin, `The version of ${repositoryPath} is frozen, not updating.`, 3);
        return false;
      }
      const localManifestJSON = await JSON.parse(localManifestContents);
      if (localManifestJSON.version !== primaryManifest.version) {
        const releaseFiles = await getRelease();
        if (releaseFiles === null)
          return false;
        if (seeIfUpdatedOnly) {
          const msg = `There is an update available for ${primaryManifest.id} from version ${localManifestJSON.version} to ${primaryManifest.version}. `;
          this.plugin.log(msg + `[Release Info](https://github.com/${repositoryPath}/releases/tag/${primaryManifest.version})`, false);
          ToastMessage(this.plugin, msg, 30, async () => {
            window.open(`https://github.com/${repositoryPath}/releases/tag/${primaryManifest.version}`);
          });
        } else {
          await this.writeReleaseFilesToPluginFolder(primaryManifest.id, releaseFiles);
          await this.plugin.app.plugins.loadManifests();
          if ((_a = this.plugin.app.plugins.plugins[primaryManifest.id]) == null ? void 0 : _a.manifest)
            await this.reloadPlugin(primaryManifest.id);
          const msg = `${primaryManifest.id}
Plugin has been updated from version ${localManifestJSON.version} to ${primaryManifest.version}. `;
          this.plugin.log(msg + `[Release Info](https://github.com/${repositoryPath}/releases/tag/${primaryManifest.version})`, false);
          ToastMessage(this.plugin, msg, 30, async () => {
            window.open(`https://github.com/${repositoryPath}/releases/tag/${primaryManifest.version}`);
          });
        }
      } else if (reportIfNotUpdted)
        ToastMessage(this.plugin, `No update available for ${repositoryPath}`, 3);
    }
    return true;
  }
  /**
   * reloads a plugin (assuming it has been enabled by user)
   * pjeby, Thanks Bro https://github.com/pjeby/hot-reload/blob/master/main.js
   * 
   * @param   {string<void>}   pluginName  name of plugin
   *
   * @return  {Promise<void>}              
   */
  async reloadPlugin(pluginName) {
    const plugins = this.plugin.app.plugins;
    try {
      await plugins.disablePlugin(pluginName);
      await plugins.enablePlugin(pluginName);
    } catch (e) {
      if (this.plugin.settings.debuggingMode)
        console.log("reload plugin", e);
    }
  }
  /**
   * updates a beta plugin
   *
   * @param   {string}   repositoryPath  repository path on GitHub
   * @param   {boolean}  onlyCheckDontUpdate only looks for update
   *
   * @return  {Promise<void>}                  
   */
  async updatePlugin(repositoryPath, onlyCheckDontUpdate = false, reportIfNotUpdted = false, forceReinstall = false) {
    const result = await this.addPlugin(repositoryPath, true, onlyCheckDontUpdate, reportIfNotUpdted, "", forceReinstall);
    if (result === false && onlyCheckDontUpdate === false)
      ToastMessage(this.plugin, `${repositoryPath}
Update of plugin failed.`);
    return result;
  }
  /**
   * walks through the list of plugins without frozen version and performs an update
   *
   * @param   {boolean}           showInfo  should this with a started/completed message - useful when ran from CP
   * @return  {Promise<void>}              
   */
  async checkForUpdatesAndInstallUpdates(showInfo = false, onlyCheckDontUpdate = false) {
    if (await isConnectedToInternet() === false) {
      console.log("BRAT: No internet detected.");
      return;
    }
    let newNotice;
    const msg1 = `Checking for plugin updates STARTED`;
    this.plugin.log(msg1, true);
    if (showInfo && this.plugin.settings.notificationsEnabled)
      newNotice = new import_obsidian7.Notice(`BRAT
${msg1}`, 3e4);
    const pluginSubListFrozenVersionNames = new Set(this.plugin.settings.pluginSubListFrozenVersion.map((f) => f.repo));
    for (const bp of this.plugin.settings.pluginList) {
      if (pluginSubListFrozenVersionNames.has(bp)) {
        continue;
      }
      await this.updatePlugin(bp, onlyCheckDontUpdate);
    }
    const msg2 = `Checking for plugin updates COMPLETED`;
    this.plugin.log(msg2, true);
    if (showInfo) {
      newNotice.hide();
      ToastMessage(this.plugin, msg2, 10);
    }
  }
  /**
   * Removes the beta plugin from the list of beta plugins (does not delete them from disk)
   *
   * @param   {string<void>}   betaPluginID  repository path
   *
   * @return  {Promise<void>}                [return description]
   */
  async deletePlugin(repositoryPath) {
    const msg = `Removed ${repositoryPath} from BRAT plugin list`;
    this.plugin.log(msg, true);
    this.plugin.settings.pluginList = this.plugin.settings.pluginList.filter((b) => b != repositoryPath);
    this.plugin.settings.pluginSubListFrozenVersion = this.plugin.settings.pluginSubListFrozenVersion.filter(
      (b) => b.repo != repositoryPath
    );
    this.plugin.saveSettings();
  }
  /**
   * Returns a list of plugins that are currently enabled or currently disabled
   *
   * @param   {boolean[]}        enabled  true for enabled plugins, false for disabled plutings
   *
   * @return  {PluginManifest[]}           manifests  of plugins
   */
  getEnabledDisabledPlugins(enabled) {
    const pl = this.plugin.app.plugins;
    const manifests = Object.values(pl.manifests);
    const enabledPlugins = Object.values(pl.plugins).map((p) => p.manifest);
    return enabled ? manifests.filter((manifest) => enabledPlugins.find((pluginName) => manifest.id === pluginName.id)) : manifests.filter((manifest) => !enabledPlugins.find((pluginName) => manifest.id === pluginName.id));
  }
};

// src/ui/icons.ts
var import_obsidian8 = require("obsidian");
function addIcons() {
  (0, import_obsidian8.addIcon)(
    "BratIcon",
    `<path fill="currentColor" stroke="currentColor"  d="M 41.667969 41.667969 C 41.667969 39.367188 39.800781 37.5 37.5 37.5 C 35.199219 37.5 33.332031 39.367188 33.332031 41.667969 C 33.332031 43.96875 35.199219 45.832031 37.5 45.832031 C 39.800781 45.832031 41.667969 43.96875 41.667969 41.667969 Z M 60.417969 58.582031 C 59.460938 58.023438 58.320312 57.867188 57.25 58.148438 C 56.179688 58.429688 55.265625 59.125 54.707031 60.082031 C 53.746094 61.777344 51.949219 62.820312 50 62.820312 C 48.050781 62.820312 46.253906 61.777344 45.292969 60.082031 C 44.734375 59.125 43.820312 58.429688 42.75 58.148438 C 41.679688 57.867188 40.539062 58.023438 39.582031 58.582031 C 37.597656 59.726562 36.910156 62.257812 38.042969 64.25 C 40.5 68.53125 45.0625 71.171875 50 71.171875 C 54.9375 71.171875 59.5 68.53125 61.957031 64.25 C 63.089844 62.257812 62.402344 59.726562 60.417969 58.582031 Z M 62.5 37.5 C 60.199219 37.5 58.332031 39.367188 58.332031 41.667969 C 58.332031 43.96875 60.199219 45.832031 62.5 45.832031 C 64.800781 45.832031 66.667969 43.96875 66.667969 41.667969 C 66.667969 39.367188 64.800781 37.5 62.5 37.5 Z M 50 8.332031 C 26.988281 8.332031 8.332031 26.988281 8.332031 50 C 8.332031 73.011719 26.988281 91.667969 50 91.667969 C 73.011719 91.667969 91.667969 73.011719 91.667969 50 C 91.667969 26.988281 73.011719 8.332031 50 8.332031 Z M 50 83.332031 C 33.988281 83.402344 20.191406 72.078125 17.136719 56.363281 C 14.078125 40.644531 22.628906 24.976562 37.5 19.042969 C 37.457031 19.636719 37.457031 20.238281 37.5 20.832031 C 37.5 27.738281 43.097656 33.332031 50 33.332031 C 52.300781 33.332031 54.167969 31.46875 54.167969 29.167969 C 54.167969 26.867188 52.300781 25 50 25 C 47.699219 25 45.832031 23.132812 45.832031 20.832031 C 45.832031 18.53125 47.699219 16.667969 50 16.667969 C 68.410156 16.667969 83.332031 31.589844 83.332031 50 C 83.332031 68.410156 68.410156 83.332031 50 83.332031 Z M 50 83.332031 " />`
  );
}

// src/utils/logging.ts
var import_obsidian9 = require("obsidian");
var import_obsidian_daily_notes_interface = __toESM(require_main());
function logger(plugin, textToLog, verboseLoggingOn = false) {
  if (plugin.settings.debuggingMode)
    console.log("BRAT: " + textToLog);
  if (plugin.settings.loggingEnabled) {
    if (plugin.settings.loggingVerboseEnabled === false && verboseLoggingOn === true) {
      return;
    } else {
      const fileName = plugin.settings.loggingPath + ".md";
      const dateOutput = "[[" + (0, import_obsidian9.moment)().format((0, import_obsidian_daily_notes_interface.getDailyNoteSettings)().format).toString() + "]] " + (0, import_obsidian9.moment)().format("HH:mm");
      const machineName = import_obsidian9.Platform.isDesktop ? window.require("os").hostname() : "MOBILE";
      let output = dateOutput + " " + machineName + " " + textToLog.replace("\n", " ") + "\n\n";
      setTimeout(async () => {
        if (await plugin.app.vault.adapter.exists(fileName) === true) {
          const fileContents = await plugin.app.vault.adapter.read(fileName);
          output = output + fileContents;
          const file = plugin.app.vault.getAbstractFileByPath(fileName);
          await plugin.app.vault.modify(file, output);
        } else
          await plugin.app.vault.create(fileName, output);
      }, 10);
    }
  }
}

// src/ui/GenericFuzzySuggester.ts
var import_obsidian10 = require("obsidian");
var GenericFuzzySuggester = class extends import_obsidian10.FuzzySuggestModal {
  constructor(plugin) {
    super(plugin.app);
    this.scope.register(["Shift"], "Enter", (evt) => this.enterTrigger(evt));
    this.scope.register(["Ctrl"], "Enter", (evt) => this.enterTrigger(evt));
  }
  setSuggesterData(suggesterData) {
    this.data = suggesterData;
  }
  async display(callBack) {
    this.callbackFunction = callBack;
    this.open();
  }
  getItems() {
    return this.data;
  }
  getItemText(item) {
    return item.display;
  }
  onChooseItem() {
    return;
  }
  // required by TS, but not using
  renderSuggestion(item, el) {
    el.createEl("div", { text: item.item.display });
  }
  enterTrigger(evt) {
    const selectedText = document.querySelector(".suggestion-item.is-selected div").textContent;
    const item = this.data.find((i) => i.display === selectedText);
    if (item) {
      this.invokeCallback(item, evt);
      this.close();
    }
  }
  onChooseSuggestion(item, evt) {
    this.invokeCallback(item.item, evt);
  }
  invokeCallback(item, evt) {
    this.callbackFunction(item, evt);
  }
};

// src/ui/PluginCommands.ts
var PluginCommands = class {
  constructor(plugin) {
    this.bratCommands = [
      {
        id: "BRAT-AddBetaPlugin",
        icon: "BratIcon",
        name: "Plugins: Add a beta plugin for testing",
        showInRibbon: true,
        callback: async () => {
          await this.plugin.betaPlugins.displayAddNewPluginModal(false, false);
        }
      },
      {
        id: "BRAT-AddBetaPluginWithFrozenVersion",
        icon: "BratIcon",
        name: "Plugins: Add a beta plugin with frozen version based on a release tag",
        showInRibbon: true,
        callback: async () => {
          await this.plugin.betaPlugins.displayAddNewPluginModal(false, true);
        }
      },
      {
        id: "BRAT-checkForUpdatesAndUpdate",
        icon: "BratIcon",
        name: "Plugins: Check for updates to all beta plugins and UPDATE",
        showInRibbon: true,
        callback: async () => {
          await this.plugin.betaPlugins.checkForUpdatesAndInstallUpdates(true, false);
        }
      },
      {
        id: "BRAT-checkForUpdatesAndDontUpdate",
        icon: "BratIcon",
        name: "Plugins: Only check for updates to beta plugins, but don't Update",
        showInRibbon: true,
        callback: async () => {
          await this.plugin.betaPlugins.checkForUpdatesAndInstallUpdates(true, true);
        }
      },
      {
        id: "BRAT-updateOnePlugin",
        icon: "BratIcon",
        name: "Plugins: Choose a single plugin version to update",
        showInRibbon: true,
        callback: async () => {
          const pluginSubListFrozenVersionNames = new Set(this.plugin.settings.pluginSubListFrozenVersion.map((f) => f.repo));
          const pluginList = Object.values(this.plugin.settings.pluginList).filter((f) => !pluginSubListFrozenVersionNames.has(f)).map((m) => {
            return { display: m, info: m };
          });
          const gfs = new GenericFuzzySuggester(this.plugin);
          gfs.setSuggesterData(pluginList);
          await gfs.display(async (results) => {
            const msg = `Checking for updates for ${results.info}`;
            this.plugin.log(msg, true);
            ToastMessage(this.plugin, `
${msg}`, 3);
            await this.plugin.betaPlugins.updatePlugin(results.info, false, true);
          });
        }
      },
      {
        id: "BRAT-reinstallOnePlugin",
        icon: "BratIcon",
        name: "Plugins: Choose a single plugin to reinstall",
        showInRibbon: true,
        callback: async () => {
          const pluginSubListFrozenVersionNames = new Set(this.plugin.settings.pluginSubListFrozenVersion.map((f) => f.repo));
          const pluginList = Object.values(this.plugin.settings.pluginList).filter((f) => !pluginSubListFrozenVersionNames.has(f)).map((m) => {
            return { display: m, info: m };
          });
          const gfs = new GenericFuzzySuggester(this.plugin);
          gfs.setSuggesterData(pluginList);
          await gfs.display(async (results) => {
            const msg = `Reinstalling ${results.info}`;
            ToastMessage(this.plugin, `
${msg}`, 3);
            this.plugin.log(msg, true);
            await this.plugin.betaPlugins.updatePlugin(results.info, false, false, true);
          });
        }
      },
      {
        id: "BRAT-restartPlugin",
        icon: "BratIcon",
        name: "Plugins: Restart a plugin that is already installed",
        showInRibbon: true,
        callback: async () => {
          const pluginList = Object.values(this.plugin.app.plugins.manifests).map((m) => {
            return { display: m.id, info: m.id };
          });
          const gfs = new GenericFuzzySuggester(this.plugin);
          gfs.setSuggesterData(pluginList);
          await gfs.display(async (results) => {
            ToastMessage(this.plugin, `${results.info}
Plugin reloading .....`, 5);
            await this.plugin.betaPlugins.reloadPlugin(results.info);
          });
        }
      },
      {
        id: "BRAT-disablePlugin",
        icon: "BratIcon",
        name: "Plugins: Disable a plugin - toggle it off",
        showInRibbon: true,
        callback: async () => {
          const pluginList = this.plugin.betaPlugins.getEnabledDisabledPlugins(true).map((manifest) => {
            return { display: `${manifest.name} (${manifest.id})`, info: manifest.id };
          });
          const gfs = new GenericFuzzySuggester(this.plugin);
          gfs.setSuggesterData(pluginList);
          await gfs.display(async (results) => {
            this.plugin.log(`${results.display} plugin disabled`, false);
            if (this.plugin.settings.debuggingMode)
              console.log(results.info);
            await this.plugin.app.plugins.disablePluginAndSave(results.info);
          });
        }
      },
      {
        id: "BRAT-enablePlugin",
        icon: "BratIcon",
        name: "Plugins: Enable a plugin - toggle it on",
        showInRibbon: true,
        callback: async () => {
          const pluginList = this.plugin.betaPlugins.getEnabledDisabledPlugins(false).map((manifest) => {
            return { display: `${manifest.name} (${manifest.id})`, info: manifest.id };
          });
          const gfs = new GenericFuzzySuggester(this.plugin);
          gfs.setSuggesterData(pluginList);
          await gfs.display(async (results) => {
            this.plugin.log(`${results.display} plugin enabled`, false);
            await this.plugin.app.plugins.enablePluginAndSave(results.info);
          });
        }
      },
      {
        id: "BRAT-openGitHubZRepository",
        icon: "BratIcon",
        name: "Plugins: Open the GitHub repository for a plugin",
        showInRibbon: true,
        callback: async () => {
          const communityPlugins = await grabCommmunityPluginList(this.plugin.settings.debuggingMode);
          const communityPluginList = Object.values(communityPlugins).map((p) => {
            return { display: `Plugin: ${p.name}  (${p.repo})`, info: p.repo };
          });
          const bratList = Object.values(this.plugin.settings.pluginList).map((p) => {
            return { display: "BRAT: " + p, info: p };
          });
          communityPluginList.forEach((si) => bratList.push(si));
          const gfs = new GenericFuzzySuggester(this.plugin);
          gfs.setSuggesterData(bratList);
          await gfs.display(async (results) => {
            if (results.info)
              window.open(`https://github.com/${results.info}`);
          });
        }
      },
      {
        id: "BRAT-openGitHubRepoTheme",
        icon: "BratIcon",
        name: "Themes: Open the GitHub repository for a theme (appearance)",
        showInRibbon: true,
        callback: async () => {
          const communityTheme = await grabCommmunityThemesList(this.plugin.settings.debuggingMode);
          const communityThemeList = Object.values(communityTheme).map((p) => {
            return { display: `Theme: ${p.name}  (${p.repo})`, info: p.repo };
          });
          const gfs = new GenericFuzzySuggester(this.plugin);
          gfs.setSuggesterData(communityThemeList);
          await gfs.display(async (results) => {
            if (results.info)
              window.open(`https://github.com/${results.info}`);
          });
        }
      },
      {
        id: "BRAT-opentPluginSettings",
        icon: "BratIcon",
        name: "Plugins: Open Plugin Settings Tab",
        showInRibbon: true,
        callback: async () => {
          const settings = this.plugin.app.setting;
          const listOfPluginSettingsTabs = Object.values(settings.pluginTabs).map((t) => {
            return { display: "Plugin: " + t.name, info: t.id };
          });
          const gfs = new GenericFuzzySuggester(this.plugin);
          const listOfCoreSettingsTabs = Object.values(settings.settingTabs).map((t) => {
            return { display: "Core: " + t.name, info: t.id };
          });
          listOfPluginSettingsTabs.forEach((si) => listOfCoreSettingsTabs.push(si));
          gfs.setSuggesterData(listOfCoreSettingsTabs);
          await gfs.display(async (results) => {
            settings.open();
            settings.openTabById(results.info);
          });
        }
      },
      {
        id: "BRAT-GrabBetaTheme",
        icon: "BratIcon",
        name: "Themes: Grab a beta theme for testing from a Github repository",
        showInRibbon: true,
        callback: async () => {
          new AddNewTheme(this.plugin).open();
        }
      },
      {
        id: "BRAT-updateBetaThemes",
        icon: "BratIcon",
        name: "Themes: Update beta themes",
        showInRibbon: true,
        callback: async () => await themesCheckAndUpdates(this.plugin, true)
      },
      {
        id: "BRAT-allCommands",
        icon: "BratIcon",
        name: "All Commands list",
        showInRibbon: false,
        callback: async () => this.ribbonDisplayCommands()
      }
    ];
    this.plugin = plugin;
    this.bratCommands.forEach(async (item) => {
      this.plugin.addCommand({
        id: item.id,
        name: item.name,
        icon: item.icon,
        callback: async () => {
          await item.callback();
        }
      });
    });
  }
  async ribbonDisplayCommands() {
    const bratCommandList = [];
    this.bratCommands.forEach((cmd) => {
      if (cmd.showInRibbon)
        bratCommandList.push({ display: cmd.name, info: cmd.callback });
    });
    const gfs = new GenericFuzzySuggester(this.plugin);
    const settings = this.plugin.app.setting;
    const listOfCoreSettingsTabs = Object.values(settings.settingTabs).map((t) => {
      return {
        display: "Core: " + t.name,
        info: async () => {
          settings.open();
          settings.openTabById(t.id);
        }
      };
    });
    const listOfPluginSettingsTabs = Object.values(settings.pluginTabs).map((t) => {
      return {
        display: "Plugin: " + t.name,
        info: async () => {
          settings.open();
          settings.openTabById(t.id);
        }
      };
    });
    bratCommandList.push({ display: "---- Core Plugin Settings ----", info: async () => {
      await this.ribbonDisplayCommands();
    } });
    listOfCoreSettingsTabs.forEach((si) => bratCommandList.push(si));
    bratCommandList.push({ display: "---- Plugin Settings ----", info: async () => {
      await this.ribbonDisplayCommands();
    } });
    listOfPluginSettingsTabs.forEach((si) => bratCommandList.push(si));
    gfs.setSuggesterData(bratCommandList);
    await gfs.display(async (results) => await results.info());
  }
};

// src/utils/BratAPI.ts
var BratAPI = class {
  constructor(plugin) {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    this.console = (logDescription, ...outputs) => {
      console.log("BRAT: " + logDescription, outputs);
    };
    this.themes = {
      themeseCheckAndUpates: async (showInfo) => {
        await themesCheckAndUpdates(this.plugin, showInfo);
      },
      themeInstallTheme: async (cssGithubRepository) => {
        const scrubbedAddress = cssGithubRepository.replace("https://github.com/", "");
        await themeSave(this.plugin, scrubbedAddress, true);
      },
      themesDelete: async (cssGithubRepository) => {
        const scrubbedAddress = cssGithubRepository.replace("https://github.com/", "");
        await themeDelete(this.plugin, scrubbedAddress);
      },
      grabCommmunityThemeCssFile: async (repositoryPath, betaVersion = false) => {
        return await grabCommmunityThemeCssFile(repositoryPath, betaVersion, this.plugin.settings.debuggingMode);
      },
      grabChecksumOfThemeCssFile: async (repositoryPath, betaVersion = false) => {
        return await grabChecksumOfThemeCssFile(repositoryPath, betaVersion, this.plugin.settings.debuggingMode);
      },
      grabLastCommitDateForAFile: async (repositoryPath, path) => {
        return await grabLastCommitDateForAFile(repositoryPath, path);
      }
    };
    this.plugin = plugin;
  }
};

// src/main.ts
var ThePlugin = class extends import_obsidian11.Plugin {
  constructor() {
    super(...arguments);
    this.appName = "Obsidian42 - Beta Reviewer's Auto-update Tool (BRAT)";
    this.appID = "obsidian42-brat";
  }
  async onload() {
    console.log("loading Obsidian42 - BRAT");
    await this.loadSettings();
    this.addSettingTab(new BratSettingsTab(this.app, this));
    this.betaPlugins = new BetaPlugins(this);
    this.commands = new PluginCommands(this);
    addIcons();
    if (this.settings.ribbonIconEnabled)
      this.showRibbonButton();
    this.app.workspace.onLayoutReady(() => {
      if (this.settings.updateAtStartup) {
        setTimeout(async () => {
          await this.betaPlugins.checkForUpdatesAndInstallUpdates(false);
        }, 6e4);
      }
      if (this.settings.updateThemesAtStartup) {
        setTimeout(async () => {
          await themesCheckAndUpdates(this, false);
        }, 12e4);
      }
      setTimeout(async () => {
        this.bratAPI = new BratAPI(this);
        globalThis.bratAPI = this.bratAPI;
      }, 500);
    });
  }
  showRibbonButton() {
    this.ribbonIcon = this.addRibbonIcon("BratIcon", "BRAT", async () => this.commands.ribbonDisplayCommands());
  }
  log(textToLog, verbose = false) {
    logger(this, textToLog, verbose);
  }
  onunload() {
    console.log("unloading " + this.appName);
  }
  async loadSettings() {
    this.settings = Object.assign({}, DEFAULT_SETTINGS, await this.loadData());
  }
  async saveSettings() {
    await this.saveData(this.settings);
  }
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsiLi4vbm9kZV9tb2R1bGVzL29ic2lkaWFuLWRhaWx5LW5vdGVzLWludGVyZmFjZS9kaXN0L21haW4uanMiLCAiLi4vc3JjL21haW4udHMiLCAiLi4vc3JjL3VpL1NldHRpbmdzVGFiLnRzIiwgIi4uL3NyYy9mZWF0dXJlcy90aGVtZXMudHMiLCAiLi4vc3JjL2ZlYXR1cmVzL2dpdGh1YlV0aWxzLnRzIiwgIi4uL3NyYy91aS9zZXR0aW5ncy50cyIsICIuLi9zcmMvdXRpbHMvbm90aWZpY2F0aW9ucy50cyIsICIuLi9zcmMvdXRpbHMvaW50ZXJuZXRjb25uZWN0aW9uLnRzIiwgIi4uL3NyYy91aS9BZGROZXdUaGVtZS50cyIsICIuLi9zcmMvdWkvUHJvbW90aW9uYWwudHMiLCAiLi4vc3JjL3VpL0FkZE5ld1BsdWdpbk1vZGFsLnRzIiwgIi4uL3NyYy9mZWF0dXJlcy9CZXRhUGx1Z2lucy50cyIsICIuLi9zcmMvdWkvaWNvbnMudHMiLCAiLi4vc3JjL3V0aWxzL2xvZ2dpbmcudHMiLCAiLi4vc3JjL3VpL0dlbmVyaWNGdXp6eVN1Z2dlc3Rlci50cyIsICIuLi9zcmMvdWkvUGx1Z2luQ29tbWFuZHMudHMiLCAiLi4vc3JjL3V0aWxzL0JyYXRBUEkudHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbIid1c2Ugc3RyaWN0JztcblxuT2JqZWN0LmRlZmluZVByb3BlcnR5KGV4cG9ydHMsICdfX2VzTW9kdWxlJywgeyB2YWx1ZTogdHJ1ZSB9KTtcblxudmFyIG9ic2lkaWFuID0gcmVxdWlyZSgnb2JzaWRpYW4nKTtcblxuY29uc3QgREVGQVVMVF9EQUlMWV9OT1RFX0ZPUk1BVCA9IFwiWVlZWS1NTS1ERFwiO1xuY29uc3QgREVGQVVMVF9XRUVLTFlfTk9URV9GT1JNQVQgPSBcImdnZ2ctW1ddd3dcIjtcbmNvbnN0IERFRkFVTFRfTU9OVEhMWV9OT1RFX0ZPUk1BVCA9IFwiWVlZWS1NTVwiO1xuY29uc3QgREVGQVVMVF9RVUFSVEVSTFlfTk9URV9GT1JNQVQgPSBcIllZWVktW1FdUVwiO1xuY29uc3QgREVGQVVMVF9ZRUFSTFlfTk9URV9GT1JNQVQgPSBcIllZWVlcIjtcblxuZnVuY3Rpb24gc2hvdWxkVXNlUGVyaW9kaWNOb3Rlc1NldHRpbmdzKHBlcmlvZGljaXR5KSB7XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICBjb25zdCBwZXJpb2RpY05vdGVzID0gd2luZG93LmFwcC5wbHVnaW5zLmdldFBsdWdpbihcInBlcmlvZGljLW5vdGVzXCIpO1xuICAgIHJldHVybiBwZXJpb2RpY05vdGVzICYmIHBlcmlvZGljTm90ZXMuc2V0dGluZ3M/LltwZXJpb2RpY2l0eV0/LmVuYWJsZWQ7XG59XG4vKipcbiAqIFJlYWQgdGhlIHVzZXIgc2V0dGluZ3MgZm9yIHRoZSBgZGFpbHktbm90ZXNgIHBsdWdpblxuICogdG8ga2VlcCBiZWhhdmlvciBvZiBjcmVhdGluZyBhIG5ldyBub3RlIGluLXN5bmMuXG4gKi9cbmZ1bmN0aW9uIGdldERhaWx5Tm90ZVNldHRpbmdzKCkge1xuICAgIHRyeSB7XG4gICAgICAgIC8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZSBAdHlwZXNjcmlwdC1lc2xpbnQvbm8tZXhwbGljaXQtYW55XG4gICAgICAgIGNvbnN0IHsgaW50ZXJuYWxQbHVnaW5zLCBwbHVnaW5zIH0gPSB3aW5kb3cuYXBwO1xuICAgICAgICBpZiAoc2hvdWxkVXNlUGVyaW9kaWNOb3Rlc1NldHRpbmdzKFwiZGFpbHlcIikpIHtcbiAgICAgICAgICAgIGNvbnN0IHsgZm9ybWF0LCBmb2xkZXIsIHRlbXBsYXRlIH0gPSBwbHVnaW5zLmdldFBsdWdpbihcInBlcmlvZGljLW5vdGVzXCIpPy5zZXR0aW5ncz8uZGFpbHkgfHwge307XG4gICAgICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgICAgIGZvcm1hdDogZm9ybWF0IHx8IERFRkFVTFRfREFJTFlfTk9URV9GT1JNQVQsXG4gICAgICAgICAgICAgICAgZm9sZGVyOiBmb2xkZXI/LnRyaW0oKSB8fCBcIlwiLFxuICAgICAgICAgICAgICAgIHRlbXBsYXRlOiB0ZW1wbGF0ZT8udHJpbSgpIHx8IFwiXCIsXG4gICAgICAgICAgICB9O1xuICAgICAgICB9XG4gICAgICAgIGNvbnN0IHsgZm9sZGVyLCBmb3JtYXQsIHRlbXBsYXRlIH0gPSBpbnRlcm5hbFBsdWdpbnMuZ2V0UGx1Z2luQnlJZChcImRhaWx5LW5vdGVzXCIpPy5pbnN0YW5jZT8ub3B0aW9ucyB8fCB7fTtcbiAgICAgICAgcmV0dXJuIHtcbiAgICAgICAgICAgIGZvcm1hdDogZm9ybWF0IHx8IERFRkFVTFRfREFJTFlfTk9URV9GT1JNQVQsXG4gICAgICAgICAgICBmb2xkZXI6IGZvbGRlcj8udHJpbSgpIHx8IFwiXCIsXG4gICAgICAgICAgICB0ZW1wbGF0ZTogdGVtcGxhdGU/LnRyaW0oKSB8fCBcIlwiLFxuICAgICAgICB9O1xuICAgIH1cbiAgICBjYXRjaCAoZXJyKSB7XG4gICAgICAgIGNvbnNvbGUuaW5mbyhcIk5vIGN1c3RvbSBkYWlseSBub3RlIHNldHRpbmdzIGZvdW5kIVwiLCBlcnIpO1xuICAgIH1cbn1cbi8qKlxuICogUmVhZCB0aGUgdXNlciBzZXR0aW5ncyBmb3IgdGhlIGB3ZWVrbHktbm90ZXNgIHBsdWdpblxuICogdG8ga2VlcCBiZWhhdmlvciBvZiBjcmVhdGluZyBhIG5ldyBub3RlIGluLXN5bmMuXG4gKi9cbmZ1bmN0aW9uIGdldFdlZWtseU5vdGVTZXR0aW5ncygpIHtcbiAgICB0cnkge1xuICAgICAgICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmUgQHR5cGVzY3JpcHQtZXNsaW50L25vLWV4cGxpY2l0LWFueVxuICAgICAgICBjb25zdCBwbHVnaW5NYW5hZ2VyID0gd2luZG93LmFwcC5wbHVnaW5zO1xuICAgICAgICBjb25zdCBjYWxlbmRhclNldHRpbmdzID0gcGx1Z2luTWFuYWdlci5nZXRQbHVnaW4oXCJjYWxlbmRhclwiKT8ub3B0aW9ucztcbiAgICAgICAgY29uc3QgcGVyaW9kaWNOb3Rlc1NldHRpbmdzID0gcGx1Z2luTWFuYWdlci5nZXRQbHVnaW4oXCJwZXJpb2RpYy1ub3Rlc1wiKT8uc2V0dGluZ3M/LndlZWtseTtcbiAgICAgICAgaWYgKHNob3VsZFVzZVBlcmlvZGljTm90ZXNTZXR0aW5ncyhcIndlZWtseVwiKSkge1xuICAgICAgICAgICAgcmV0dXJuIHtcbiAgICAgICAgICAgICAgICBmb3JtYXQ6IHBlcmlvZGljTm90ZXNTZXR0aW5ncy5mb3JtYXQgfHwgREVGQVVMVF9XRUVLTFlfTk9URV9GT1JNQVQsXG4gICAgICAgICAgICAgICAgZm9sZGVyOiBwZXJpb2RpY05vdGVzU2V0dGluZ3MuZm9sZGVyPy50cmltKCkgfHwgXCJcIixcbiAgICAgICAgICAgICAgICB0ZW1wbGF0ZTogcGVyaW9kaWNOb3Rlc1NldHRpbmdzLnRlbXBsYXRlPy50cmltKCkgfHwgXCJcIixcbiAgICAgICAgICAgIH07XG4gICAgICAgIH1cbiAgICAgICAgY29uc3Qgc2V0dGluZ3MgPSBjYWxlbmRhclNldHRpbmdzIHx8IHt9O1xuICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgZm9ybWF0OiBzZXR0aW5ncy53ZWVrbHlOb3RlRm9ybWF0IHx8IERFRkFVTFRfV0VFS0xZX05PVEVfRk9STUFULFxuICAgICAgICAgICAgZm9sZGVyOiBzZXR0aW5ncy53ZWVrbHlOb3RlRm9sZGVyPy50cmltKCkgfHwgXCJcIixcbiAgICAgICAgICAgIHRlbXBsYXRlOiBzZXR0aW5ncy53ZWVrbHlOb3RlVGVtcGxhdGU/LnRyaW0oKSB8fCBcIlwiLFxuICAgICAgICB9O1xuICAgIH1cbiAgICBjYXRjaCAoZXJyKSB7XG4gICAgICAgIGNvbnNvbGUuaW5mbyhcIk5vIGN1c3RvbSB3ZWVrbHkgbm90ZSBzZXR0aW5ncyBmb3VuZCFcIiwgZXJyKTtcbiAgICB9XG59XG4vKipcbiAqIFJlYWQgdGhlIHVzZXIgc2V0dGluZ3MgZm9yIHRoZSBgcGVyaW9kaWMtbm90ZXNgIHBsdWdpblxuICogdG8ga2VlcCBiZWhhdmlvciBvZiBjcmVhdGluZyBhIG5ldyBub3RlIGluLXN5bmMuXG4gKi9cbmZ1bmN0aW9uIGdldE1vbnRobHlOb3RlU2V0dGluZ3MoKSB7XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICBjb25zdCBwbHVnaW5NYW5hZ2VyID0gd2luZG93LmFwcC5wbHVnaW5zO1xuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IHNldHRpbmdzID0gKHNob3VsZFVzZVBlcmlvZGljTm90ZXNTZXR0aW5ncyhcIm1vbnRobHlcIikgJiZcbiAgICAgICAgICAgIHBsdWdpbk1hbmFnZXIuZ2V0UGx1Z2luKFwicGVyaW9kaWMtbm90ZXNcIik/LnNldHRpbmdzPy5tb250aGx5KSB8fFxuICAgICAgICAgICAge307XG4gICAgICAgIHJldHVybiB7XG4gICAgICAgICAgICBmb3JtYXQ6IHNldHRpbmdzLmZvcm1hdCB8fCBERUZBVUxUX01PTlRITFlfTk9URV9GT1JNQVQsXG4gICAgICAgICAgICBmb2xkZXI6IHNldHRpbmdzLmZvbGRlcj8udHJpbSgpIHx8IFwiXCIsXG4gICAgICAgICAgICB0ZW1wbGF0ZTogc2V0dGluZ3MudGVtcGxhdGU/LnRyaW0oKSB8fCBcIlwiLFxuICAgICAgICB9O1xuICAgIH1cbiAgICBjYXRjaCAoZXJyKSB7XG4gICAgICAgIGNvbnNvbGUuaW5mbyhcIk5vIGN1c3RvbSBtb250aGx5IG5vdGUgc2V0dGluZ3MgZm91bmQhXCIsIGVycik7XG4gICAgfVxufVxuLyoqXG4gKiBSZWFkIHRoZSB1c2VyIHNldHRpbmdzIGZvciB0aGUgYHBlcmlvZGljLW5vdGVzYCBwbHVnaW5cbiAqIHRvIGtlZXAgYmVoYXZpb3Igb2YgY3JlYXRpbmcgYSBuZXcgbm90ZSBpbi1zeW5jLlxuICovXG5mdW5jdGlvbiBnZXRRdWFydGVybHlOb3RlU2V0dGluZ3MoKSB7XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICBjb25zdCBwbHVnaW5NYW5hZ2VyID0gd2luZG93LmFwcC5wbHVnaW5zO1xuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IHNldHRpbmdzID0gKHNob3VsZFVzZVBlcmlvZGljTm90ZXNTZXR0aW5ncyhcInF1YXJ0ZXJseVwiKSAmJlxuICAgICAgICAgICAgcGx1Z2luTWFuYWdlci5nZXRQbHVnaW4oXCJwZXJpb2RpYy1ub3Rlc1wiKT8uc2V0dGluZ3M/LnF1YXJ0ZXJseSkgfHxcbiAgICAgICAgICAgIHt9O1xuICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgZm9ybWF0OiBzZXR0aW5ncy5mb3JtYXQgfHwgREVGQVVMVF9RVUFSVEVSTFlfTk9URV9GT1JNQVQsXG4gICAgICAgICAgICBmb2xkZXI6IHNldHRpbmdzLmZvbGRlcj8udHJpbSgpIHx8IFwiXCIsXG4gICAgICAgICAgICB0ZW1wbGF0ZTogc2V0dGluZ3MudGVtcGxhdGU/LnRyaW0oKSB8fCBcIlwiLFxuICAgICAgICB9O1xuICAgIH1cbiAgICBjYXRjaCAoZXJyKSB7XG4gICAgICAgIGNvbnNvbGUuaW5mbyhcIk5vIGN1c3RvbSBxdWFydGVybHkgbm90ZSBzZXR0aW5ncyBmb3VuZCFcIiwgZXJyKTtcbiAgICB9XG59XG4vKipcbiAqIFJlYWQgdGhlIHVzZXIgc2V0dGluZ3MgZm9yIHRoZSBgcGVyaW9kaWMtbm90ZXNgIHBsdWdpblxuICogdG8ga2VlcCBiZWhhdmlvciBvZiBjcmVhdGluZyBhIG5ldyBub3RlIGluLXN5bmMuXG4gKi9cbmZ1bmN0aW9uIGdldFllYXJseU5vdGVTZXR0aW5ncygpIHtcbiAgICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmUgQHR5cGVzY3JpcHQtZXNsaW50L25vLWV4cGxpY2l0LWFueVxuICAgIGNvbnN0IHBsdWdpbk1hbmFnZXIgPSB3aW5kb3cuYXBwLnBsdWdpbnM7XG4gICAgdHJ5IHtcbiAgICAgICAgY29uc3Qgc2V0dGluZ3MgPSAoc2hvdWxkVXNlUGVyaW9kaWNOb3Rlc1NldHRpbmdzKFwieWVhcmx5XCIpICYmXG4gICAgICAgICAgICBwbHVnaW5NYW5hZ2VyLmdldFBsdWdpbihcInBlcmlvZGljLW5vdGVzXCIpPy5zZXR0aW5ncz8ueWVhcmx5KSB8fFxuICAgICAgICAgICAge307XG4gICAgICAgIHJldHVybiB7XG4gICAgICAgICAgICBmb3JtYXQ6IHNldHRpbmdzLmZvcm1hdCB8fCBERUZBVUxUX1lFQVJMWV9OT1RFX0ZPUk1BVCxcbiAgICAgICAgICAgIGZvbGRlcjogc2V0dGluZ3MuZm9sZGVyPy50cmltKCkgfHwgXCJcIixcbiAgICAgICAgICAgIHRlbXBsYXRlOiBzZXR0aW5ncy50ZW1wbGF0ZT8udHJpbSgpIHx8IFwiXCIsXG4gICAgICAgIH07XG4gICAgfVxuICAgIGNhdGNoIChlcnIpIHtcbiAgICAgICAgY29uc29sZS5pbmZvKFwiTm8gY3VzdG9tIHllYXJseSBub3RlIHNldHRpbmdzIGZvdW5kIVwiLCBlcnIpO1xuICAgIH1cbn1cblxuLy8gQ3JlZGl0OiBAY3JlYXRpb25peC9wYXRoLmpzXG5mdW5jdGlvbiBqb2luKC4uLnBhcnRTZWdtZW50cykge1xuICAgIC8vIFNwbGl0IHRoZSBpbnB1dHMgaW50byBhIGxpc3Qgb2YgcGF0aCBjb21tYW5kcy5cbiAgICBsZXQgcGFydHMgPSBbXTtcbiAgICBmb3IgKGxldCBpID0gMCwgbCA9IHBhcnRTZWdtZW50cy5sZW5ndGg7IGkgPCBsOyBpKyspIHtcbiAgICAgICAgcGFydHMgPSBwYXJ0cy5jb25jYXQocGFydFNlZ21lbnRzW2ldLnNwbGl0KFwiL1wiKSk7XG4gICAgfVxuICAgIC8vIEludGVycHJldCB0aGUgcGF0aCBjb21tYW5kcyB0byBnZXQgdGhlIG5ldyByZXNvbHZlZCBwYXRoLlxuICAgIGNvbnN0IG5ld1BhcnRzID0gW107XG4gICAgZm9yIChsZXQgaSA9IDAsIGwgPSBwYXJ0cy5sZW5ndGg7IGkgPCBsOyBpKyspIHtcbiAgICAgICAgY29uc3QgcGFydCA9IHBhcnRzW2ldO1xuICAgICAgICAvLyBSZW1vdmUgbGVhZGluZyBhbmQgdHJhaWxpbmcgc2xhc2hlc1xuICAgICAgICAvLyBBbHNvIHJlbW92ZSBcIi5cIiBzZWdtZW50c1xuICAgICAgICBpZiAoIXBhcnQgfHwgcGFydCA9PT0gXCIuXCIpXG4gICAgICAgICAgICBjb250aW51ZTtcbiAgICAgICAgLy8gUHVzaCBuZXcgcGF0aCBzZWdtZW50cy5cbiAgICAgICAgZWxzZVxuICAgICAgICAgICAgbmV3UGFydHMucHVzaChwYXJ0KTtcbiAgICB9XG4gICAgLy8gUHJlc2VydmUgdGhlIGluaXRpYWwgc2xhc2ggaWYgdGhlcmUgd2FzIG9uZS5cbiAgICBpZiAocGFydHNbMF0gPT09IFwiXCIpXG4gICAgICAgIG5ld1BhcnRzLnVuc2hpZnQoXCJcIik7XG4gICAgLy8gVHVybiBiYWNrIGludG8gYSBzaW5nbGUgc3RyaW5nIHBhdGguXG4gICAgcmV0dXJuIG5ld1BhcnRzLmpvaW4oXCIvXCIpO1xufVxuZnVuY3Rpb24gYmFzZW5hbWUoZnVsbFBhdGgpIHtcbiAgICBsZXQgYmFzZSA9IGZ1bGxQYXRoLnN1YnN0cmluZyhmdWxsUGF0aC5sYXN0SW5kZXhPZihcIi9cIikgKyAxKTtcbiAgICBpZiAoYmFzZS5sYXN0SW5kZXhPZihcIi5cIikgIT0gLTEpXG4gICAgICAgIGJhc2UgPSBiYXNlLnN1YnN0cmluZygwLCBiYXNlLmxhc3RJbmRleE9mKFwiLlwiKSk7XG4gICAgcmV0dXJuIGJhc2U7XG59XG5hc3luYyBmdW5jdGlvbiBlbnN1cmVGb2xkZXJFeGlzdHMocGF0aCkge1xuICAgIGNvbnN0IGRpcnMgPSBwYXRoLnJlcGxhY2UoL1xcXFwvZywgXCIvXCIpLnNwbGl0KFwiL1wiKTtcbiAgICBkaXJzLnBvcCgpOyAvLyByZW1vdmUgYmFzZW5hbWVcbiAgICBpZiAoZGlycy5sZW5ndGgpIHtcbiAgICAgICAgY29uc3QgZGlyID0gam9pbiguLi5kaXJzKTtcbiAgICAgICAgaWYgKCF3aW5kb3cuYXBwLnZhdWx0LmdldEFic3RyYWN0RmlsZUJ5UGF0aChkaXIpKSB7XG4gICAgICAgICAgICBhd2FpdCB3aW5kb3cuYXBwLnZhdWx0LmNyZWF0ZUZvbGRlcihkaXIpO1xuICAgICAgICB9XG4gICAgfVxufVxuYXN5bmMgZnVuY3Rpb24gZ2V0Tm90ZVBhdGgoZGlyZWN0b3J5LCBmaWxlbmFtZSkge1xuICAgIGlmICghZmlsZW5hbWUuZW5kc1dpdGgoXCIubWRcIikpIHtcbiAgICAgICAgZmlsZW5hbWUgKz0gXCIubWRcIjtcbiAgICB9XG4gICAgY29uc3QgcGF0aCA9IG9ic2lkaWFuLm5vcm1hbGl6ZVBhdGgoam9pbihkaXJlY3RvcnksIGZpbGVuYW1lKSk7XG4gICAgYXdhaXQgZW5zdXJlRm9sZGVyRXhpc3RzKHBhdGgpO1xuICAgIHJldHVybiBwYXRoO1xufVxuYXN5bmMgZnVuY3Rpb24gZ2V0VGVtcGxhdGVJbmZvKHRlbXBsYXRlKSB7XG4gICAgY29uc3QgeyBtZXRhZGF0YUNhY2hlLCB2YXVsdCB9ID0gd2luZG93LmFwcDtcbiAgICBjb25zdCB0ZW1wbGF0ZVBhdGggPSBvYnNpZGlhbi5ub3JtYWxpemVQYXRoKHRlbXBsYXRlKTtcbiAgICBpZiAodGVtcGxhdGVQYXRoID09PSBcIi9cIikge1xuICAgICAgICByZXR1cm4gUHJvbWlzZS5yZXNvbHZlKFtcIlwiLCBudWxsXSk7XG4gICAgfVxuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IHRlbXBsYXRlRmlsZSA9IG1ldGFkYXRhQ2FjaGUuZ2V0Rmlyc3RMaW5rcGF0aERlc3QodGVtcGxhdGVQYXRoLCBcIlwiKTtcbiAgICAgICAgY29uc3QgY29udGVudHMgPSBhd2FpdCB2YXVsdC5jYWNoZWRSZWFkKHRlbXBsYXRlRmlsZSk7XG4gICAgICAgIC8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZSBAdHlwZXNjcmlwdC1lc2xpbnQvbm8tZXhwbGljaXQtYW55XG4gICAgICAgIGNvbnN0IElGb2xkSW5mbyA9IHdpbmRvdy5hcHAuZm9sZE1hbmFnZXIubG9hZCh0ZW1wbGF0ZUZpbGUpO1xuICAgICAgICByZXR1cm4gW2NvbnRlbnRzLCBJRm9sZEluZm9dO1xuICAgIH1cbiAgICBjYXRjaCAoZXJyKSB7XG4gICAgICAgIGNvbnNvbGUuZXJyb3IoYEZhaWxlZCB0byByZWFkIHRoZSBkYWlseSBub3RlIHRlbXBsYXRlICcke3RlbXBsYXRlUGF0aH0nYCwgZXJyKTtcbiAgICAgICAgbmV3IG9ic2lkaWFuLk5vdGljZShcIkZhaWxlZCB0byByZWFkIHRoZSBkYWlseSBub3RlIHRlbXBsYXRlXCIpO1xuICAgICAgICByZXR1cm4gW1wiXCIsIG51bGxdO1xuICAgIH1cbn1cblxuLyoqXG4gKiBkYXRlVUlEIGlzIGEgd2F5IG9mIHdlZWtseSBpZGVudGlmeWluZyBkYWlseS93ZWVrbHkvbW9udGhseSBub3Rlcy5cbiAqIFRoZXkgYXJlIHByZWZpeGVkIHdpdGggdGhlIGdyYW51bGFyaXR5IHRvIGF2b2lkIGFtYmlndWl0eS5cbiAqL1xuZnVuY3Rpb24gZ2V0RGF0ZVVJRChkYXRlLCBncmFudWxhcml0eSA9IFwiZGF5XCIpIHtcbiAgICBjb25zdCB0cyA9IGRhdGUuY2xvbmUoKS5zdGFydE9mKGdyYW51bGFyaXR5KS5mb3JtYXQoKTtcbiAgICByZXR1cm4gYCR7Z3JhbnVsYXJpdHl9LSR7dHN9YDtcbn1cbmZ1bmN0aW9uIHJlbW92ZUVzY2FwZWRDaGFyYWN0ZXJzKGZvcm1hdCkge1xuICAgIHJldHVybiBmb3JtYXQucmVwbGFjZSgvXFxbW15cXF1dKlxcXS9nLCBcIlwiKTsgLy8gcmVtb3ZlIGV2ZXJ5dGhpbmcgd2l0aGluIGJyYWNrZXRzXG59XG4vKipcbiAqIFhYWDogV2hlbiBwYXJzaW5nIGRhdGVzIHRoYXQgY29udGFpbiBib3RoIHdlZWsgbnVtYmVycyBhbmQgbW9udGhzLFxuICogTW9tZW50IGNob3NlcyB0byBpZ25vcmUgdGhlIHdlZWsgbnVtYmVycy4gRm9yIHRoZSB3ZWVrIGRhdGVVSUQsIHdlXG4gKiB3YW50IHRoZSBvcHBvc2l0ZSBiZWhhdmlvci4gU3RyaXAgdGhlIE1NTSBmcm9tIHRoZSBmb3JtYXQgdG8gcGF0Y2guXG4gKi9cbmZ1bmN0aW9uIGlzRm9ybWF0QW1iaWd1b3VzKGZvcm1hdCwgZ3JhbnVsYXJpdHkpIHtcbiAgICBpZiAoZ3JhbnVsYXJpdHkgPT09IFwid2Vla1wiKSB7XG4gICAgICAgIGNvbnN0IGNsZWFuRm9ybWF0ID0gcmVtb3ZlRXNjYXBlZENoYXJhY3RlcnMoZm9ybWF0KTtcbiAgICAgICAgcmV0dXJuICgvd3sxLDJ9L2kudGVzdChjbGVhbkZvcm1hdCkgJiZcbiAgICAgICAgICAgICgvTXsxLDR9Ly50ZXN0KGNsZWFuRm9ybWF0KSB8fCAvRHsxLDR9Ly50ZXN0KGNsZWFuRm9ybWF0KSkpO1xuICAgIH1cbiAgICByZXR1cm4gZmFsc2U7XG59XG5mdW5jdGlvbiBnZXREYXRlRnJvbUZpbGUoZmlsZSwgZ3JhbnVsYXJpdHkpIHtcbiAgICByZXR1cm4gZ2V0RGF0ZUZyb21GaWxlbmFtZShmaWxlLmJhc2VuYW1lLCBncmFudWxhcml0eSk7XG59XG5mdW5jdGlvbiBnZXREYXRlRnJvbVBhdGgocGF0aCwgZ3JhbnVsYXJpdHkpIHtcbiAgICByZXR1cm4gZ2V0RGF0ZUZyb21GaWxlbmFtZShiYXNlbmFtZShwYXRoKSwgZ3JhbnVsYXJpdHkpO1xufVxuZnVuY3Rpb24gZ2V0RGF0ZUZyb21GaWxlbmFtZShmaWxlbmFtZSwgZ3JhbnVsYXJpdHkpIHtcbiAgICBjb25zdCBnZXRTZXR0aW5ncyA9IHtcbiAgICAgICAgZGF5OiBnZXREYWlseU5vdGVTZXR0aW5ncyxcbiAgICAgICAgd2VlazogZ2V0V2Vla2x5Tm90ZVNldHRpbmdzLFxuICAgICAgICBtb250aDogZ2V0TW9udGhseU5vdGVTZXR0aW5ncyxcbiAgICAgICAgcXVhcnRlcjogZ2V0UXVhcnRlcmx5Tm90ZVNldHRpbmdzLFxuICAgICAgICB5ZWFyOiBnZXRZZWFybHlOb3RlU2V0dGluZ3MsXG4gICAgfTtcbiAgICBjb25zdCBmb3JtYXQgPSBnZXRTZXR0aW5nc1tncmFudWxhcml0eV0oKS5mb3JtYXQuc3BsaXQoXCIvXCIpLnBvcCgpO1xuICAgIGNvbnN0IG5vdGVEYXRlID0gd2luZG93Lm1vbWVudChmaWxlbmFtZSwgZm9ybWF0LCB0cnVlKTtcbiAgICBpZiAoIW5vdGVEYXRlLmlzVmFsaWQoKSkge1xuICAgICAgICByZXR1cm4gbnVsbDtcbiAgICB9XG4gICAgaWYgKGlzRm9ybWF0QW1iaWd1b3VzKGZvcm1hdCwgZ3JhbnVsYXJpdHkpKSB7XG4gICAgICAgIGlmIChncmFudWxhcml0eSA9PT0gXCJ3ZWVrXCIpIHtcbiAgICAgICAgICAgIGNvbnN0IGNsZWFuRm9ybWF0ID0gcmVtb3ZlRXNjYXBlZENoYXJhY3RlcnMoZm9ybWF0KTtcbiAgICAgICAgICAgIGlmICgvd3sxLDJ9L2kudGVzdChjbGVhbkZvcm1hdCkpIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gd2luZG93Lm1vbWVudChmaWxlbmFtZSwgXG4gICAgICAgICAgICAgICAgLy8gSWYgZm9ybWF0IGNvbnRhaW5zIHdlZWssIHJlbW92ZSBkYXkgJiBtb250aCBmb3JtYXR0aW5nXG4gICAgICAgICAgICAgICAgZm9ybWF0LnJlcGxhY2UoL017MSw0fS9nLCBcIlwiKS5yZXBsYWNlKC9EezEsNH0vZywgXCJcIiksIGZhbHNlKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgIH1cbiAgICByZXR1cm4gbm90ZURhdGU7XG59XG5cbmNsYXNzIERhaWx5Tm90ZXNGb2xkZXJNaXNzaW5nRXJyb3IgZXh0ZW5kcyBFcnJvciB7XG59XG4vKipcbiAqIFRoaXMgZnVuY3Rpb24gbWltaWNzIHRoZSBiZWhhdmlvciBvZiB0aGUgZGFpbHktbm90ZXMgcGx1Z2luXG4gKiBzbyBpdCB3aWxsIHJlcGxhY2Uge3tkYXRlfX0sIHt7dGl0bGV9fSwgYW5kIHt7dGltZX19IHdpdGggdGhlXG4gKiBmb3JtYXR0ZWQgdGltZXN0YW1wLlxuICpcbiAqIE5vdGU6IGl0IGhhcyBhbiBhZGRlZCBib251cyB0aGF0IGl0J3Mgbm90ICd0b2RheScgc3BlY2lmaWMuXG4gKi9cbmFzeW5jIGZ1bmN0aW9uIGNyZWF0ZURhaWx5Tm90ZShkYXRlKSB7XG4gICAgY29uc3QgYXBwID0gd2luZG93LmFwcDtcbiAgICBjb25zdCB7IHZhdWx0IH0gPSBhcHA7XG4gICAgY29uc3QgbW9tZW50ID0gd2luZG93Lm1vbWVudDtcbiAgICBjb25zdCB7IHRlbXBsYXRlLCBmb3JtYXQsIGZvbGRlciB9ID0gZ2V0RGFpbHlOb3RlU2V0dGluZ3MoKTtcbiAgICBjb25zdCBbdGVtcGxhdGVDb250ZW50cywgSUZvbGRJbmZvXSA9IGF3YWl0IGdldFRlbXBsYXRlSW5mbyh0ZW1wbGF0ZSk7XG4gICAgY29uc3QgZmlsZW5hbWUgPSBkYXRlLmZvcm1hdChmb3JtYXQpO1xuICAgIGNvbnN0IG5vcm1hbGl6ZWRQYXRoID0gYXdhaXQgZ2V0Tm90ZVBhdGgoZm9sZGVyLCBmaWxlbmFtZSk7XG4gICAgdHJ5IHtcbiAgICAgICAgY29uc3QgY3JlYXRlZEZpbGUgPSBhd2FpdCB2YXVsdC5jcmVhdGUobm9ybWFsaXplZFBhdGgsIHRlbXBsYXRlQ29udGVudHNcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccypkYXRlXFxzKn19L2dpLCBmaWxlbmFtZSlcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccyp0aW1lXFxzKn19L2dpLCBtb21lbnQoKS5mb3JtYXQoXCJISDptbVwiKSlcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccyp0aXRsZVxccyp9fS9naSwgZmlsZW5hbWUpXG4gICAgICAgICAgICAucmVwbGFjZSgve3tcXHMqKGRhdGV8dGltZSlcXHMqKChbKy1dXFxkKykoW3lxbXdkaHNdKSk/XFxzKig6Lis/KT99fS9naSwgKF8sIF90aW1lT3JEYXRlLCBjYWxjLCB0aW1lRGVsdGEsIHVuaXQsIG1vbWVudEZvcm1hdCkgPT4ge1xuICAgICAgICAgICAgY29uc3Qgbm93ID0gbW9tZW50KCk7XG4gICAgICAgICAgICBjb25zdCBjdXJyZW50RGF0ZSA9IGRhdGUuY2xvbmUoKS5zZXQoe1xuICAgICAgICAgICAgICAgIGhvdXI6IG5vdy5nZXQoXCJob3VyXCIpLFxuICAgICAgICAgICAgICAgIG1pbnV0ZTogbm93LmdldChcIm1pbnV0ZVwiKSxcbiAgICAgICAgICAgICAgICBzZWNvbmQ6IG5vdy5nZXQoXCJzZWNvbmRcIiksXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIGlmIChjYWxjKSB7XG4gICAgICAgICAgICAgICAgY3VycmVudERhdGUuYWRkKHBhcnNlSW50KHRpbWVEZWx0YSwgMTApLCB1bml0KTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGlmIChtb21lbnRGb3JtYXQpIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gY3VycmVudERhdGUuZm9ybWF0KG1vbWVudEZvcm1hdC5zdWJzdHJpbmcoMSkudHJpbSgpKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHJldHVybiBjdXJyZW50RGF0ZS5mb3JtYXQoZm9ybWF0KTtcbiAgICAgICAgfSlcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccyp5ZXN0ZXJkYXlcXHMqfX0vZ2ksIGRhdGUuY2xvbmUoKS5zdWJ0cmFjdCgxLCBcImRheVwiKS5mb3JtYXQoZm9ybWF0KSlcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccyp0b21vcnJvd1xccyp9fS9naSwgZGF0ZS5jbG9uZSgpLmFkZCgxLCBcImRcIikuZm9ybWF0KGZvcm1hdCkpKTtcbiAgICAgICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICAgICAgYXBwLmZvbGRNYW5hZ2VyLnNhdmUoY3JlYXRlZEZpbGUsIElGb2xkSW5mbyk7XG4gICAgICAgIHJldHVybiBjcmVhdGVkRmlsZTtcbiAgICB9XG4gICAgY2F0Y2ggKGVycikge1xuICAgICAgICBjb25zb2xlLmVycm9yKGBGYWlsZWQgdG8gY3JlYXRlIGZpbGU6ICcke25vcm1hbGl6ZWRQYXRofSdgLCBlcnIpO1xuICAgICAgICBuZXcgb2JzaWRpYW4uTm90aWNlKFwiVW5hYmxlIHRvIGNyZWF0ZSBuZXcgZmlsZS5cIik7XG4gICAgfVxufVxuZnVuY3Rpb24gZ2V0RGFpbHlOb3RlKGRhdGUsIGRhaWx5Tm90ZXMpIHtcbiAgICByZXR1cm4gZGFpbHlOb3Rlc1tnZXREYXRlVUlEKGRhdGUsIFwiZGF5XCIpXSA/PyBudWxsO1xufVxuZnVuY3Rpb24gZ2V0QWxsRGFpbHlOb3RlcygpIHtcbiAgICAvKipcbiAgICAgKiBGaW5kIGFsbCBkYWlseSBub3RlcyBpbiB0aGUgZGFpbHkgbm90ZSBmb2xkZXJcbiAgICAgKi9cbiAgICBjb25zdCB7IHZhdWx0IH0gPSB3aW5kb3cuYXBwO1xuICAgIGNvbnN0IHsgZm9sZGVyIH0gPSBnZXREYWlseU5vdGVTZXR0aW5ncygpO1xuICAgIGNvbnN0IGRhaWx5Tm90ZXNGb2xkZXIgPSB2YXVsdC5nZXRBYnN0cmFjdEZpbGVCeVBhdGgob2JzaWRpYW4ubm9ybWFsaXplUGF0aChmb2xkZXIpKTtcbiAgICBpZiAoIWRhaWx5Tm90ZXNGb2xkZXIpIHtcbiAgICAgICAgdGhyb3cgbmV3IERhaWx5Tm90ZXNGb2xkZXJNaXNzaW5nRXJyb3IoXCJGYWlsZWQgdG8gZmluZCBkYWlseSBub3RlcyBmb2xkZXJcIik7XG4gICAgfVxuICAgIGNvbnN0IGRhaWx5Tm90ZXMgPSB7fTtcbiAgICBvYnNpZGlhbi5WYXVsdC5yZWN1cnNlQ2hpbGRyZW4oZGFpbHlOb3Rlc0ZvbGRlciwgKG5vdGUpID0+IHtcbiAgICAgICAgaWYgKG5vdGUgaW5zdGFuY2VvZiBvYnNpZGlhbi5URmlsZSkge1xuICAgICAgICAgICAgY29uc3QgZGF0ZSA9IGdldERhdGVGcm9tRmlsZShub3RlLCBcImRheVwiKTtcbiAgICAgICAgICAgIGlmIChkYXRlKSB7XG4gICAgICAgICAgICAgICAgY29uc3QgZGF0ZVN0cmluZyA9IGdldERhdGVVSUQoZGF0ZSwgXCJkYXlcIik7XG4gICAgICAgICAgICAgICAgZGFpbHlOb3Rlc1tkYXRlU3RyaW5nXSA9IG5vdGU7XG4gICAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICB9KTtcbiAgICByZXR1cm4gZGFpbHlOb3Rlcztcbn1cblxuY2xhc3MgV2Vla2x5Tm90ZXNGb2xkZXJNaXNzaW5nRXJyb3IgZXh0ZW5kcyBFcnJvciB7XG59XG5mdW5jdGlvbiBnZXREYXlzT2ZXZWVrKCkge1xuICAgIGNvbnN0IHsgbW9tZW50IH0gPSB3aW5kb3c7XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICBsZXQgd2Vla1N0YXJ0ID0gbW9tZW50LmxvY2FsZURhdGEoKS5fd2Vlay5kb3c7XG4gICAgY29uc3QgZGF5c09mV2VlayA9IFtcbiAgICAgICAgXCJzdW5kYXlcIixcbiAgICAgICAgXCJtb25kYXlcIixcbiAgICAgICAgXCJ0dWVzZGF5XCIsXG4gICAgICAgIFwid2VkbmVzZGF5XCIsXG4gICAgICAgIFwidGh1cnNkYXlcIixcbiAgICAgICAgXCJmcmlkYXlcIixcbiAgICAgICAgXCJzYXR1cmRheVwiLFxuICAgIF07XG4gICAgd2hpbGUgKHdlZWtTdGFydCkge1xuICAgICAgICBkYXlzT2ZXZWVrLnB1c2goZGF5c09mV2Vlay5zaGlmdCgpKTtcbiAgICAgICAgd2Vla1N0YXJ0LS07XG4gICAgfVxuICAgIHJldHVybiBkYXlzT2ZXZWVrO1xufVxuZnVuY3Rpb24gZ2V0RGF5T2ZXZWVrTnVtZXJpY2FsVmFsdWUoZGF5T2ZXZWVrTmFtZSkge1xuICAgIHJldHVybiBnZXREYXlzT2ZXZWVrKCkuaW5kZXhPZihkYXlPZldlZWtOYW1lLnRvTG93ZXJDYXNlKCkpO1xufVxuYXN5bmMgZnVuY3Rpb24gY3JlYXRlV2Vla2x5Tm90ZShkYXRlKSB7XG4gICAgY29uc3QgeyB2YXVsdCB9ID0gd2luZG93LmFwcDtcbiAgICBjb25zdCB7IHRlbXBsYXRlLCBmb3JtYXQsIGZvbGRlciB9ID0gZ2V0V2Vla2x5Tm90ZVNldHRpbmdzKCk7XG4gICAgY29uc3QgW3RlbXBsYXRlQ29udGVudHMsIElGb2xkSW5mb10gPSBhd2FpdCBnZXRUZW1wbGF0ZUluZm8odGVtcGxhdGUpO1xuICAgIGNvbnN0IGZpbGVuYW1lID0gZGF0ZS5mb3JtYXQoZm9ybWF0KTtcbiAgICBjb25zdCBub3JtYWxpemVkUGF0aCA9IGF3YWl0IGdldE5vdGVQYXRoKGZvbGRlciwgZmlsZW5hbWUpO1xuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IGNyZWF0ZWRGaWxlID0gYXdhaXQgdmF1bHQuY3JlYXRlKG5vcm1hbGl6ZWRQYXRoLCB0ZW1wbGF0ZUNvbnRlbnRzXG4gICAgICAgICAgICAucmVwbGFjZSgve3tcXHMqKGRhdGV8dGltZSlcXHMqKChbKy1dXFxkKykoW3lxbXdkaHNdKSk/XFxzKig6Lis/KT99fS9naSwgKF8sIF90aW1lT3JEYXRlLCBjYWxjLCB0aW1lRGVsdGEsIHVuaXQsIG1vbWVudEZvcm1hdCkgPT4ge1xuICAgICAgICAgICAgY29uc3Qgbm93ID0gd2luZG93Lm1vbWVudCgpO1xuICAgICAgICAgICAgY29uc3QgY3VycmVudERhdGUgPSBkYXRlLmNsb25lKCkuc2V0KHtcbiAgICAgICAgICAgICAgICBob3VyOiBub3cuZ2V0KFwiaG91clwiKSxcbiAgICAgICAgICAgICAgICBtaW51dGU6IG5vdy5nZXQoXCJtaW51dGVcIiksXG4gICAgICAgICAgICAgICAgc2Vjb25kOiBub3cuZ2V0KFwic2Vjb25kXCIpLFxuICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICBpZiAoY2FsYykge1xuICAgICAgICAgICAgICAgIGN1cnJlbnREYXRlLmFkZChwYXJzZUludCh0aW1lRGVsdGEsIDEwKSwgdW5pdCk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICBpZiAobW9tZW50Rm9ybWF0KSB7XG4gICAgICAgICAgICAgICAgcmV0dXJuIGN1cnJlbnREYXRlLmZvcm1hdChtb21lbnRGb3JtYXQuc3Vic3RyaW5nKDEpLnRyaW0oKSk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICByZXR1cm4gY3VycmVudERhdGUuZm9ybWF0KGZvcm1hdCk7XG4gICAgICAgIH0pXG4gICAgICAgICAgICAucmVwbGFjZSgve3tcXHMqdGl0bGVcXHMqfX0vZ2ksIGZpbGVuYW1lKVxuICAgICAgICAgICAgLnJlcGxhY2UoL3t7XFxzKnRpbWVcXHMqfX0vZ2ksIHdpbmRvdy5tb21lbnQoKS5mb3JtYXQoXCJISDptbVwiKSlcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccyooc3VuZGF5fG1vbmRheXx0dWVzZGF5fHdlZG5lc2RheXx0aHVyc2RheXxmcmlkYXl8c2F0dXJkYXkpXFxzKjooLio/KX19L2dpLCAoXywgZGF5T2ZXZWVrLCBtb21lbnRGb3JtYXQpID0+IHtcbiAgICAgICAgICAgIGNvbnN0IGRheSA9IGdldERheU9mV2Vla051bWVyaWNhbFZhbHVlKGRheU9mV2Vlayk7XG4gICAgICAgICAgICByZXR1cm4gZGF0ZS53ZWVrZGF5KGRheSkuZm9ybWF0KG1vbWVudEZvcm1hdC50cmltKCkpO1xuICAgICAgICB9KSk7XG4gICAgICAgIC8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZSBAdHlwZXNjcmlwdC1lc2xpbnQvbm8tZXhwbGljaXQtYW55XG4gICAgICAgIHdpbmRvdy5hcHAuZm9sZE1hbmFnZXIuc2F2ZShjcmVhdGVkRmlsZSwgSUZvbGRJbmZvKTtcbiAgICAgICAgcmV0dXJuIGNyZWF0ZWRGaWxlO1xuICAgIH1cbiAgICBjYXRjaCAoZXJyKSB7XG4gICAgICAgIGNvbnNvbGUuZXJyb3IoYEZhaWxlZCB0byBjcmVhdGUgZmlsZTogJyR7bm9ybWFsaXplZFBhdGh9J2AsIGVycik7XG4gICAgICAgIG5ldyBvYnNpZGlhbi5Ob3RpY2UoXCJVbmFibGUgdG8gY3JlYXRlIG5ldyBmaWxlLlwiKTtcbiAgICB9XG59XG5mdW5jdGlvbiBnZXRXZWVrbHlOb3RlKGRhdGUsIHdlZWtseU5vdGVzKSB7XG4gICAgcmV0dXJuIHdlZWtseU5vdGVzW2dldERhdGVVSUQoZGF0ZSwgXCJ3ZWVrXCIpXSA/PyBudWxsO1xufVxuZnVuY3Rpb24gZ2V0QWxsV2Vla2x5Tm90ZXMoKSB7XG4gICAgY29uc3Qgd2Vla2x5Tm90ZXMgPSB7fTtcbiAgICBpZiAoIWFwcEhhc1dlZWtseU5vdGVzUGx1Z2luTG9hZGVkKCkpIHtcbiAgICAgICAgcmV0dXJuIHdlZWtseU5vdGVzO1xuICAgIH1cbiAgICBjb25zdCB7IHZhdWx0IH0gPSB3aW5kb3cuYXBwO1xuICAgIGNvbnN0IHsgZm9sZGVyIH0gPSBnZXRXZWVrbHlOb3RlU2V0dGluZ3MoKTtcbiAgICBjb25zdCB3ZWVrbHlOb3Rlc0ZvbGRlciA9IHZhdWx0LmdldEFic3RyYWN0RmlsZUJ5UGF0aChvYnNpZGlhbi5ub3JtYWxpemVQYXRoKGZvbGRlcikpO1xuICAgIGlmICghd2Vla2x5Tm90ZXNGb2xkZXIpIHtcbiAgICAgICAgdGhyb3cgbmV3IFdlZWtseU5vdGVzRm9sZGVyTWlzc2luZ0Vycm9yKFwiRmFpbGVkIHRvIGZpbmQgd2Vla2x5IG5vdGVzIGZvbGRlclwiKTtcbiAgICB9XG4gICAgb2JzaWRpYW4uVmF1bHQucmVjdXJzZUNoaWxkcmVuKHdlZWtseU5vdGVzRm9sZGVyLCAobm90ZSkgPT4ge1xuICAgICAgICBpZiAobm90ZSBpbnN0YW5jZW9mIG9ic2lkaWFuLlRGaWxlKSB7XG4gICAgICAgICAgICBjb25zdCBkYXRlID0gZ2V0RGF0ZUZyb21GaWxlKG5vdGUsIFwid2Vla1wiKTtcbiAgICAgICAgICAgIGlmIChkYXRlKSB7XG4gICAgICAgICAgICAgICAgY29uc3QgZGF0ZVN0cmluZyA9IGdldERhdGVVSUQoZGF0ZSwgXCJ3ZWVrXCIpO1xuICAgICAgICAgICAgICAgIHdlZWtseU5vdGVzW2RhdGVTdHJpbmddID0gbm90ZTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiB3ZWVrbHlOb3Rlcztcbn1cblxuY2xhc3MgTW9udGhseU5vdGVzRm9sZGVyTWlzc2luZ0Vycm9yIGV4dGVuZHMgRXJyb3Ige1xufVxuLyoqXG4gKiBUaGlzIGZ1bmN0aW9uIG1pbWljcyB0aGUgYmVoYXZpb3Igb2YgdGhlIGRhaWx5LW5vdGVzIHBsdWdpblxuICogc28gaXQgd2lsbCByZXBsYWNlIHt7ZGF0ZX19LCB7e3RpdGxlfX0sIGFuZCB7e3RpbWV9fSB3aXRoIHRoZVxuICogZm9ybWF0dGVkIHRpbWVzdGFtcC5cbiAqXG4gKiBOb3RlOiBpdCBoYXMgYW4gYWRkZWQgYm9udXMgdGhhdCBpdCdzIG5vdCAndG9kYXknIHNwZWNpZmljLlxuICovXG5hc3luYyBmdW5jdGlvbiBjcmVhdGVNb250aGx5Tm90ZShkYXRlKSB7XG4gICAgY29uc3QgeyB2YXVsdCB9ID0gd2luZG93LmFwcDtcbiAgICBjb25zdCB7IHRlbXBsYXRlLCBmb3JtYXQsIGZvbGRlciB9ID0gZ2V0TW9udGhseU5vdGVTZXR0aW5ncygpO1xuICAgIGNvbnN0IFt0ZW1wbGF0ZUNvbnRlbnRzLCBJRm9sZEluZm9dID0gYXdhaXQgZ2V0VGVtcGxhdGVJbmZvKHRlbXBsYXRlKTtcbiAgICBjb25zdCBmaWxlbmFtZSA9IGRhdGUuZm9ybWF0KGZvcm1hdCk7XG4gICAgY29uc3Qgbm9ybWFsaXplZFBhdGggPSBhd2FpdCBnZXROb3RlUGF0aChmb2xkZXIsIGZpbGVuYW1lKTtcbiAgICB0cnkge1xuICAgICAgICBjb25zdCBjcmVhdGVkRmlsZSA9IGF3YWl0IHZhdWx0LmNyZWF0ZShub3JtYWxpemVkUGF0aCwgdGVtcGxhdGVDb250ZW50c1xuICAgICAgICAgICAgLnJlcGxhY2UoL3t7XFxzKihkYXRlfHRpbWUpXFxzKigoWystXVxcZCspKFt5cW13ZGhzXSkpP1xccyooOi4rPyk/fX0vZ2ksIChfLCBfdGltZU9yRGF0ZSwgY2FsYywgdGltZURlbHRhLCB1bml0LCBtb21lbnRGb3JtYXQpID0+IHtcbiAgICAgICAgICAgIGNvbnN0IG5vdyA9IHdpbmRvdy5tb21lbnQoKTtcbiAgICAgICAgICAgIGNvbnN0IGN1cnJlbnREYXRlID0gZGF0ZS5jbG9uZSgpLnNldCh7XG4gICAgICAgICAgICAgICAgaG91cjogbm93LmdldChcImhvdXJcIiksXG4gICAgICAgICAgICAgICAgbWludXRlOiBub3cuZ2V0KFwibWludXRlXCIpLFxuICAgICAgICAgICAgICAgIHNlY29uZDogbm93LmdldChcInNlY29uZFwiKSxcbiAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgaWYgKGNhbGMpIHtcbiAgICAgICAgICAgICAgICBjdXJyZW50RGF0ZS5hZGQocGFyc2VJbnQodGltZURlbHRhLCAxMCksIHVuaXQpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgaWYgKG1vbWVudEZvcm1hdCkge1xuICAgICAgICAgICAgICAgIHJldHVybiBjdXJyZW50RGF0ZS5mb3JtYXQobW9tZW50Rm9ybWF0LnN1YnN0cmluZygxKS50cmltKCkpO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgcmV0dXJuIGN1cnJlbnREYXRlLmZvcm1hdChmb3JtYXQpO1xuICAgICAgICB9KVxuICAgICAgICAgICAgLnJlcGxhY2UoL3t7XFxzKmRhdGVcXHMqfX0vZ2ksIGZpbGVuYW1lKVxuICAgICAgICAgICAgLnJlcGxhY2UoL3t7XFxzKnRpbWVcXHMqfX0vZ2ksIHdpbmRvdy5tb21lbnQoKS5mb3JtYXQoXCJISDptbVwiKSlcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccyp0aXRsZVxccyp9fS9naSwgZmlsZW5hbWUpKTtcbiAgICAgICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICAgICAgd2luZG93LmFwcC5mb2xkTWFuYWdlci5zYXZlKGNyZWF0ZWRGaWxlLCBJRm9sZEluZm8pO1xuICAgICAgICByZXR1cm4gY3JlYXRlZEZpbGU7XG4gICAgfVxuICAgIGNhdGNoIChlcnIpIHtcbiAgICAgICAgY29uc29sZS5lcnJvcihgRmFpbGVkIHRvIGNyZWF0ZSBmaWxlOiAnJHtub3JtYWxpemVkUGF0aH0nYCwgZXJyKTtcbiAgICAgICAgbmV3IG9ic2lkaWFuLk5vdGljZShcIlVuYWJsZSB0byBjcmVhdGUgbmV3IGZpbGUuXCIpO1xuICAgIH1cbn1cbmZ1bmN0aW9uIGdldE1vbnRobHlOb3RlKGRhdGUsIG1vbnRobHlOb3Rlcykge1xuICAgIHJldHVybiBtb250aGx5Tm90ZXNbZ2V0RGF0ZVVJRChkYXRlLCBcIm1vbnRoXCIpXSA/PyBudWxsO1xufVxuZnVuY3Rpb24gZ2V0QWxsTW9udGhseU5vdGVzKCkge1xuICAgIGNvbnN0IG1vbnRobHlOb3RlcyA9IHt9O1xuICAgIGlmICghYXBwSGFzTW9udGhseU5vdGVzUGx1Z2luTG9hZGVkKCkpIHtcbiAgICAgICAgcmV0dXJuIG1vbnRobHlOb3RlcztcbiAgICB9XG4gICAgY29uc3QgeyB2YXVsdCB9ID0gd2luZG93LmFwcDtcbiAgICBjb25zdCB7IGZvbGRlciB9ID0gZ2V0TW9udGhseU5vdGVTZXR0aW5ncygpO1xuICAgIGNvbnN0IG1vbnRobHlOb3Rlc0ZvbGRlciA9IHZhdWx0LmdldEFic3RyYWN0RmlsZUJ5UGF0aChvYnNpZGlhbi5ub3JtYWxpemVQYXRoKGZvbGRlcikpO1xuICAgIGlmICghbW9udGhseU5vdGVzRm9sZGVyKSB7XG4gICAgICAgIHRocm93IG5ldyBNb250aGx5Tm90ZXNGb2xkZXJNaXNzaW5nRXJyb3IoXCJGYWlsZWQgdG8gZmluZCBtb250aGx5IG5vdGVzIGZvbGRlclwiKTtcbiAgICB9XG4gICAgb2JzaWRpYW4uVmF1bHQucmVjdXJzZUNoaWxkcmVuKG1vbnRobHlOb3Rlc0ZvbGRlciwgKG5vdGUpID0+IHtcbiAgICAgICAgaWYgKG5vdGUgaW5zdGFuY2VvZiBvYnNpZGlhbi5URmlsZSkge1xuICAgICAgICAgICAgY29uc3QgZGF0ZSA9IGdldERhdGVGcm9tRmlsZShub3RlLCBcIm1vbnRoXCIpO1xuICAgICAgICAgICAgaWYgKGRhdGUpIHtcbiAgICAgICAgICAgICAgICBjb25zdCBkYXRlU3RyaW5nID0gZ2V0RGF0ZVVJRChkYXRlLCBcIm1vbnRoXCIpO1xuICAgICAgICAgICAgICAgIG1vbnRobHlOb3Rlc1tkYXRlU3RyaW5nXSA9IG5vdGU7XG4gICAgICAgICAgICB9XG4gICAgICAgIH1cbiAgICB9KTtcbiAgICByZXR1cm4gbW9udGhseU5vdGVzO1xufVxuXG5jbGFzcyBRdWFydGVybHlOb3Rlc0ZvbGRlck1pc3NpbmdFcnJvciBleHRlbmRzIEVycm9yIHtcbn1cbi8qKlxuICogVGhpcyBmdW5jdGlvbiBtaW1pY3MgdGhlIGJlaGF2aW9yIG9mIHRoZSBkYWlseS1ub3RlcyBwbHVnaW5cbiAqIHNvIGl0IHdpbGwgcmVwbGFjZSB7e2RhdGV9fSwge3t0aXRsZX19LCBhbmQge3t0aW1lfX0gd2l0aCB0aGVcbiAqIGZvcm1hdHRlZCB0aW1lc3RhbXAuXG4gKlxuICogTm90ZTogaXQgaGFzIGFuIGFkZGVkIGJvbnVzIHRoYXQgaXQncyBub3QgJ3RvZGF5JyBzcGVjaWZpYy5cbiAqL1xuYXN5bmMgZnVuY3Rpb24gY3JlYXRlUXVhcnRlcmx5Tm90ZShkYXRlKSB7XG4gICAgY29uc3QgeyB2YXVsdCB9ID0gd2luZG93LmFwcDtcbiAgICBjb25zdCB7IHRlbXBsYXRlLCBmb3JtYXQsIGZvbGRlciB9ID0gZ2V0UXVhcnRlcmx5Tm90ZVNldHRpbmdzKCk7XG4gICAgY29uc3QgW3RlbXBsYXRlQ29udGVudHMsIElGb2xkSW5mb10gPSBhd2FpdCBnZXRUZW1wbGF0ZUluZm8odGVtcGxhdGUpO1xuICAgIGNvbnN0IGZpbGVuYW1lID0gZGF0ZS5mb3JtYXQoZm9ybWF0KTtcbiAgICBjb25zdCBub3JtYWxpemVkUGF0aCA9IGF3YWl0IGdldE5vdGVQYXRoKGZvbGRlciwgZmlsZW5hbWUpO1xuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IGNyZWF0ZWRGaWxlID0gYXdhaXQgdmF1bHQuY3JlYXRlKG5vcm1hbGl6ZWRQYXRoLCB0ZW1wbGF0ZUNvbnRlbnRzXG4gICAgICAgICAgICAucmVwbGFjZSgve3tcXHMqKGRhdGV8dGltZSlcXHMqKChbKy1dXFxkKykoW3lxbXdkaHNdKSk/XFxzKig6Lis/KT99fS9naSwgKF8sIF90aW1lT3JEYXRlLCBjYWxjLCB0aW1lRGVsdGEsIHVuaXQsIG1vbWVudEZvcm1hdCkgPT4ge1xuICAgICAgICAgICAgY29uc3Qgbm93ID0gd2luZG93Lm1vbWVudCgpO1xuICAgICAgICAgICAgY29uc3QgY3VycmVudERhdGUgPSBkYXRlLmNsb25lKCkuc2V0KHtcbiAgICAgICAgICAgICAgICBob3VyOiBub3cuZ2V0KFwiaG91clwiKSxcbiAgICAgICAgICAgICAgICBtaW51dGU6IG5vdy5nZXQoXCJtaW51dGVcIiksXG4gICAgICAgICAgICAgICAgc2Vjb25kOiBub3cuZ2V0KFwic2Vjb25kXCIpLFxuICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICBpZiAoY2FsYykge1xuICAgICAgICAgICAgICAgIGN1cnJlbnREYXRlLmFkZChwYXJzZUludCh0aW1lRGVsdGEsIDEwKSwgdW5pdCk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICBpZiAobW9tZW50Rm9ybWF0KSB7XG4gICAgICAgICAgICAgICAgcmV0dXJuIGN1cnJlbnREYXRlLmZvcm1hdChtb21lbnRGb3JtYXQuc3Vic3RyaW5nKDEpLnRyaW0oKSk7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICByZXR1cm4gY3VycmVudERhdGUuZm9ybWF0KGZvcm1hdCk7XG4gICAgICAgIH0pXG4gICAgICAgICAgICAucmVwbGFjZSgve3tcXHMqZGF0ZVxccyp9fS9naSwgZmlsZW5hbWUpXG4gICAgICAgICAgICAucmVwbGFjZSgve3tcXHMqdGltZVxccyp9fS9naSwgd2luZG93Lm1vbWVudCgpLmZvcm1hdChcIkhIOm1tXCIpKVxuICAgICAgICAgICAgLnJlcGxhY2UoL3t7XFxzKnRpdGxlXFxzKn19L2dpLCBmaWxlbmFtZSkpO1xuICAgICAgICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmUgQHR5cGVzY3JpcHQtZXNsaW50L25vLWV4cGxpY2l0LWFueVxuICAgICAgICB3aW5kb3cuYXBwLmZvbGRNYW5hZ2VyLnNhdmUoY3JlYXRlZEZpbGUsIElGb2xkSW5mbyk7XG4gICAgICAgIHJldHVybiBjcmVhdGVkRmlsZTtcbiAgICB9XG4gICAgY2F0Y2ggKGVycikge1xuICAgICAgICBjb25zb2xlLmVycm9yKGBGYWlsZWQgdG8gY3JlYXRlIGZpbGU6ICcke25vcm1hbGl6ZWRQYXRofSdgLCBlcnIpO1xuICAgICAgICBuZXcgb2JzaWRpYW4uTm90aWNlKFwiVW5hYmxlIHRvIGNyZWF0ZSBuZXcgZmlsZS5cIik7XG4gICAgfVxufVxuZnVuY3Rpb24gZ2V0UXVhcnRlcmx5Tm90ZShkYXRlLCBxdWFydGVybHkpIHtcbiAgICByZXR1cm4gcXVhcnRlcmx5W2dldERhdGVVSUQoZGF0ZSwgXCJxdWFydGVyXCIpXSA/PyBudWxsO1xufVxuZnVuY3Rpb24gZ2V0QWxsUXVhcnRlcmx5Tm90ZXMoKSB7XG4gICAgY29uc3QgcXVhcnRlcmx5ID0ge307XG4gICAgaWYgKCFhcHBIYXNRdWFydGVybHlOb3Rlc1BsdWdpbkxvYWRlZCgpKSB7XG4gICAgICAgIHJldHVybiBxdWFydGVybHk7XG4gICAgfVxuICAgIGNvbnN0IHsgdmF1bHQgfSA9IHdpbmRvdy5hcHA7XG4gICAgY29uc3QgeyBmb2xkZXIgfSA9IGdldFF1YXJ0ZXJseU5vdGVTZXR0aW5ncygpO1xuICAgIGNvbnN0IHF1YXJ0ZXJseUZvbGRlciA9IHZhdWx0LmdldEFic3RyYWN0RmlsZUJ5UGF0aChvYnNpZGlhbi5ub3JtYWxpemVQYXRoKGZvbGRlcikpO1xuICAgIGlmICghcXVhcnRlcmx5Rm9sZGVyKSB7XG4gICAgICAgIHRocm93IG5ldyBRdWFydGVybHlOb3Rlc0ZvbGRlck1pc3NpbmdFcnJvcihcIkZhaWxlZCB0byBmaW5kIHF1YXJ0ZXJseSBub3RlcyBmb2xkZXJcIik7XG4gICAgfVxuICAgIG9ic2lkaWFuLlZhdWx0LnJlY3Vyc2VDaGlsZHJlbihxdWFydGVybHlGb2xkZXIsIChub3RlKSA9PiB7XG4gICAgICAgIGlmIChub3RlIGluc3RhbmNlb2Ygb2JzaWRpYW4uVEZpbGUpIHtcbiAgICAgICAgICAgIGNvbnN0IGRhdGUgPSBnZXREYXRlRnJvbUZpbGUobm90ZSwgXCJxdWFydGVyXCIpO1xuICAgICAgICAgICAgaWYgKGRhdGUpIHtcbiAgICAgICAgICAgICAgICBjb25zdCBkYXRlU3RyaW5nID0gZ2V0RGF0ZVVJRChkYXRlLCBcInF1YXJ0ZXJcIik7XG4gICAgICAgICAgICAgICAgcXVhcnRlcmx5W2RhdGVTdHJpbmddID0gbm90ZTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiBxdWFydGVybHk7XG59XG5cbmNsYXNzIFllYXJseU5vdGVzRm9sZGVyTWlzc2luZ0Vycm9yIGV4dGVuZHMgRXJyb3Ige1xufVxuLyoqXG4gKiBUaGlzIGZ1bmN0aW9uIG1pbWljcyB0aGUgYmVoYXZpb3Igb2YgdGhlIGRhaWx5LW5vdGVzIHBsdWdpblxuICogc28gaXQgd2lsbCByZXBsYWNlIHt7ZGF0ZX19LCB7e3RpdGxlfX0sIGFuZCB7e3RpbWV9fSB3aXRoIHRoZVxuICogZm9ybWF0dGVkIHRpbWVzdGFtcC5cbiAqXG4gKiBOb3RlOiBpdCBoYXMgYW4gYWRkZWQgYm9udXMgdGhhdCBpdCdzIG5vdCAndG9kYXknIHNwZWNpZmljLlxuICovXG5hc3luYyBmdW5jdGlvbiBjcmVhdGVZZWFybHlOb3RlKGRhdGUpIHtcbiAgICBjb25zdCB7IHZhdWx0IH0gPSB3aW5kb3cuYXBwO1xuICAgIGNvbnN0IHsgdGVtcGxhdGUsIGZvcm1hdCwgZm9sZGVyIH0gPSBnZXRZZWFybHlOb3RlU2V0dGluZ3MoKTtcbiAgICBjb25zdCBbdGVtcGxhdGVDb250ZW50cywgSUZvbGRJbmZvXSA9IGF3YWl0IGdldFRlbXBsYXRlSW5mbyh0ZW1wbGF0ZSk7XG4gICAgY29uc3QgZmlsZW5hbWUgPSBkYXRlLmZvcm1hdChmb3JtYXQpO1xuICAgIGNvbnN0IG5vcm1hbGl6ZWRQYXRoID0gYXdhaXQgZ2V0Tm90ZVBhdGgoZm9sZGVyLCBmaWxlbmFtZSk7XG4gICAgdHJ5IHtcbiAgICAgICAgY29uc3QgY3JlYXRlZEZpbGUgPSBhd2FpdCB2YXVsdC5jcmVhdGUobm9ybWFsaXplZFBhdGgsIHRlbXBsYXRlQ29udGVudHNcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccyooZGF0ZXx0aW1lKVxccyooKFsrLV1cXGQrKShbeXFtd2Roc10pKT9cXHMqKDouKz8pP319L2dpLCAoXywgX3RpbWVPckRhdGUsIGNhbGMsIHRpbWVEZWx0YSwgdW5pdCwgbW9tZW50Rm9ybWF0KSA9PiB7XG4gICAgICAgICAgICBjb25zdCBub3cgPSB3aW5kb3cubW9tZW50KCk7XG4gICAgICAgICAgICBjb25zdCBjdXJyZW50RGF0ZSA9IGRhdGUuY2xvbmUoKS5zZXQoe1xuICAgICAgICAgICAgICAgIGhvdXI6IG5vdy5nZXQoXCJob3VyXCIpLFxuICAgICAgICAgICAgICAgIG1pbnV0ZTogbm93LmdldChcIm1pbnV0ZVwiKSxcbiAgICAgICAgICAgICAgICBzZWNvbmQ6IG5vdy5nZXQoXCJzZWNvbmRcIiksXG4gICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIGlmIChjYWxjKSB7XG4gICAgICAgICAgICAgICAgY3VycmVudERhdGUuYWRkKHBhcnNlSW50KHRpbWVEZWx0YSwgMTApLCB1bml0KTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIGlmIChtb21lbnRGb3JtYXQpIHtcbiAgICAgICAgICAgICAgICByZXR1cm4gY3VycmVudERhdGUuZm9ybWF0KG1vbWVudEZvcm1hdC5zdWJzdHJpbmcoMSkudHJpbSgpKTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgICAgIHJldHVybiBjdXJyZW50RGF0ZS5mb3JtYXQoZm9ybWF0KTtcbiAgICAgICAgfSlcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccypkYXRlXFxzKn19L2dpLCBmaWxlbmFtZSlcbiAgICAgICAgICAgIC5yZXBsYWNlKC97e1xccyp0aW1lXFxzKn19L2dpLCB3aW5kb3cubW9tZW50KCkuZm9ybWF0KFwiSEg6bW1cIikpXG4gICAgICAgICAgICAucmVwbGFjZSgve3tcXHMqdGl0bGVcXHMqfX0vZ2ksIGZpbGVuYW1lKSk7XG4gICAgICAgIC8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZSBAdHlwZXNjcmlwdC1lc2xpbnQvbm8tZXhwbGljaXQtYW55XG4gICAgICAgIHdpbmRvdy5hcHAuZm9sZE1hbmFnZXIuc2F2ZShjcmVhdGVkRmlsZSwgSUZvbGRJbmZvKTtcbiAgICAgICAgcmV0dXJuIGNyZWF0ZWRGaWxlO1xuICAgIH1cbiAgICBjYXRjaCAoZXJyKSB7XG4gICAgICAgIGNvbnNvbGUuZXJyb3IoYEZhaWxlZCB0byBjcmVhdGUgZmlsZTogJyR7bm9ybWFsaXplZFBhdGh9J2AsIGVycik7XG4gICAgICAgIG5ldyBvYnNpZGlhbi5Ob3RpY2UoXCJVbmFibGUgdG8gY3JlYXRlIG5ldyBmaWxlLlwiKTtcbiAgICB9XG59XG5mdW5jdGlvbiBnZXRZZWFybHlOb3RlKGRhdGUsIHllYXJseU5vdGVzKSB7XG4gICAgcmV0dXJuIHllYXJseU5vdGVzW2dldERhdGVVSUQoZGF0ZSwgXCJ5ZWFyXCIpXSA/PyBudWxsO1xufVxuZnVuY3Rpb24gZ2V0QWxsWWVhcmx5Tm90ZXMoKSB7XG4gICAgY29uc3QgeWVhcmx5Tm90ZXMgPSB7fTtcbiAgICBpZiAoIWFwcEhhc1llYXJseU5vdGVzUGx1Z2luTG9hZGVkKCkpIHtcbiAgICAgICAgcmV0dXJuIHllYXJseU5vdGVzO1xuICAgIH1cbiAgICBjb25zdCB7IHZhdWx0IH0gPSB3aW5kb3cuYXBwO1xuICAgIGNvbnN0IHsgZm9sZGVyIH0gPSBnZXRZZWFybHlOb3RlU2V0dGluZ3MoKTtcbiAgICBjb25zdCB5ZWFybHlOb3Rlc0ZvbGRlciA9IHZhdWx0LmdldEFic3RyYWN0RmlsZUJ5UGF0aChvYnNpZGlhbi5ub3JtYWxpemVQYXRoKGZvbGRlcikpO1xuICAgIGlmICgheWVhcmx5Tm90ZXNGb2xkZXIpIHtcbiAgICAgICAgdGhyb3cgbmV3IFllYXJseU5vdGVzRm9sZGVyTWlzc2luZ0Vycm9yKFwiRmFpbGVkIHRvIGZpbmQgeWVhcmx5IG5vdGVzIGZvbGRlclwiKTtcbiAgICB9XG4gICAgb2JzaWRpYW4uVmF1bHQucmVjdXJzZUNoaWxkcmVuKHllYXJseU5vdGVzRm9sZGVyLCAobm90ZSkgPT4ge1xuICAgICAgICBpZiAobm90ZSBpbnN0YW5jZW9mIG9ic2lkaWFuLlRGaWxlKSB7XG4gICAgICAgICAgICBjb25zdCBkYXRlID0gZ2V0RGF0ZUZyb21GaWxlKG5vdGUsIFwieWVhclwiKTtcbiAgICAgICAgICAgIGlmIChkYXRlKSB7XG4gICAgICAgICAgICAgICAgY29uc3QgZGF0ZVN0cmluZyA9IGdldERhdGVVSUQoZGF0ZSwgXCJ5ZWFyXCIpO1xuICAgICAgICAgICAgICAgIHllYXJseU5vdGVzW2RhdGVTdHJpbmddID0gbm90ZTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuICAgIH0pO1xuICAgIHJldHVybiB5ZWFybHlOb3Rlcztcbn1cblxuZnVuY3Rpb24gYXBwSGFzRGFpbHlOb3Rlc1BsdWdpbkxvYWRlZCgpIHtcbiAgICBjb25zdCB7IGFwcCB9ID0gd2luZG93O1xuICAgIC8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZSBAdHlwZXNjcmlwdC1lc2xpbnQvbm8tZXhwbGljaXQtYW55XG4gICAgY29uc3QgZGFpbHlOb3Rlc1BsdWdpbiA9IGFwcC5pbnRlcm5hbFBsdWdpbnMucGx1Z2luc1tcImRhaWx5LW5vdGVzXCJdO1xuICAgIGlmIChkYWlseU5vdGVzUGx1Z2luICYmIGRhaWx5Tm90ZXNQbHVnaW4uZW5hYmxlZCkge1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICBjb25zdCBwZXJpb2RpY05vdGVzID0gYXBwLnBsdWdpbnMuZ2V0UGx1Z2luKFwicGVyaW9kaWMtbm90ZXNcIik7XG4gICAgcmV0dXJuIHBlcmlvZGljTm90ZXMgJiYgcGVyaW9kaWNOb3Rlcy5zZXR0aW5ncz8uZGFpbHk/LmVuYWJsZWQ7XG59XG4vKipcbiAqIFhYWDogXCJXZWVrbHkgTm90ZXNcIiBsaXZlIGluIGVpdGhlciB0aGUgQ2FsZW5kYXIgcGx1Z2luIG9yIHRoZSBwZXJpb2RpYy1ub3RlcyBwbHVnaW4uXG4gKiBDaGVjayBib3RoIHVudGlsIHRoZSB3ZWVrbHkgbm90ZXMgZmVhdHVyZSBpcyByZW1vdmVkIGZyb20gdGhlIENhbGVuZGFyIHBsdWdpbi5cbiAqL1xuZnVuY3Rpb24gYXBwSGFzV2Vla2x5Tm90ZXNQbHVnaW5Mb2FkZWQoKSB7XG4gICAgY29uc3QgeyBhcHAgfSA9IHdpbmRvdztcbiAgICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmUgQHR5cGVzY3JpcHQtZXNsaW50L25vLWV4cGxpY2l0LWFueVxuICAgIGlmIChhcHAucGx1Z2lucy5nZXRQbHVnaW4oXCJjYWxlbmRhclwiKSkge1xuICAgICAgICByZXR1cm4gdHJ1ZTtcbiAgICB9XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICBjb25zdCBwZXJpb2RpY05vdGVzID0gYXBwLnBsdWdpbnMuZ2V0UGx1Z2luKFwicGVyaW9kaWMtbm90ZXNcIik7XG4gICAgcmV0dXJuIHBlcmlvZGljTm90ZXMgJiYgcGVyaW9kaWNOb3Rlcy5zZXR0aW5ncz8ud2Vla2x5Py5lbmFibGVkO1xufVxuZnVuY3Rpb24gYXBwSGFzTW9udGhseU5vdGVzUGx1Z2luTG9hZGVkKCkge1xuICAgIGNvbnN0IHsgYXBwIH0gPSB3aW5kb3c7XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICBjb25zdCBwZXJpb2RpY05vdGVzID0gYXBwLnBsdWdpbnMuZ2V0UGx1Z2luKFwicGVyaW9kaWMtbm90ZXNcIik7XG4gICAgcmV0dXJuIHBlcmlvZGljTm90ZXMgJiYgcGVyaW9kaWNOb3Rlcy5zZXR0aW5ncz8ubW9udGhseT8uZW5hYmxlZDtcbn1cbmZ1bmN0aW9uIGFwcEhhc1F1YXJ0ZXJseU5vdGVzUGx1Z2luTG9hZGVkKCkge1xuICAgIGNvbnN0IHsgYXBwIH0gPSB3aW5kb3c7XG4gICAgLy8gZXNsaW50LWRpc2FibGUtbmV4dC1saW5lIEB0eXBlc2NyaXB0LWVzbGludC9uby1leHBsaWNpdC1hbnlcbiAgICBjb25zdCBwZXJpb2RpY05vdGVzID0gYXBwLnBsdWdpbnMuZ2V0UGx1Z2luKFwicGVyaW9kaWMtbm90ZXNcIik7XG4gICAgcmV0dXJuIHBlcmlvZGljTm90ZXMgJiYgcGVyaW9kaWNOb3Rlcy5zZXR0aW5ncz8ucXVhcnRlcmx5Py5lbmFibGVkO1xufVxuZnVuY3Rpb24gYXBwSGFzWWVhcmx5Tm90ZXNQbHVnaW5Mb2FkZWQoKSB7XG4gICAgY29uc3QgeyBhcHAgfSA9IHdpbmRvdztcbiAgICAvLyBlc2xpbnQtZGlzYWJsZS1uZXh0LWxpbmUgQHR5cGVzY3JpcHQtZXNsaW50L25vLWV4cGxpY2l0LWFueVxuICAgIGNvbnN0IHBlcmlvZGljTm90ZXMgPSBhcHAucGx1Z2lucy5nZXRQbHVnaW4oXCJwZXJpb2RpYy1ub3Rlc1wiKTtcbiAgICByZXR1cm4gcGVyaW9kaWNOb3RlcyAmJiBwZXJpb2RpY05vdGVzLnNldHRpbmdzPy55ZWFybHk/LmVuYWJsZWQ7XG59XG5mdW5jdGlvbiBnZXRQZXJpb2RpY05vdGVTZXR0aW5ncyhncmFudWxhcml0eSkge1xuICAgIGNvbnN0IGdldFNldHRpbmdzID0ge1xuICAgICAgICBkYXk6IGdldERhaWx5Tm90ZVNldHRpbmdzLFxuICAgICAgICB3ZWVrOiBnZXRXZWVrbHlOb3RlU2V0dGluZ3MsXG4gICAgICAgIG1vbnRoOiBnZXRNb250aGx5Tm90ZVNldHRpbmdzLFxuICAgICAgICBxdWFydGVyOiBnZXRRdWFydGVybHlOb3RlU2V0dGluZ3MsXG4gICAgICAgIHllYXI6IGdldFllYXJseU5vdGVTZXR0aW5ncyxcbiAgICB9W2dyYW51bGFyaXR5XTtcbiAgICByZXR1cm4gZ2V0U2V0dGluZ3MoKTtcbn1cbmZ1bmN0aW9uIGNyZWF0ZVBlcmlvZGljTm90ZShncmFudWxhcml0eSwgZGF0ZSkge1xuICAgIGNvbnN0IGNyZWF0ZUZuID0ge1xuICAgICAgICBkYXk6IGNyZWF0ZURhaWx5Tm90ZSxcbiAgICAgICAgbW9udGg6IGNyZWF0ZU1vbnRobHlOb3RlLFxuICAgICAgICB3ZWVrOiBjcmVhdGVXZWVrbHlOb3RlLFxuICAgIH07XG4gICAgcmV0dXJuIGNyZWF0ZUZuW2dyYW51bGFyaXR5XShkYXRlKTtcbn1cblxuZXhwb3J0cy5ERUZBVUxUX0RBSUxZX05PVEVfRk9STUFUID0gREVGQVVMVF9EQUlMWV9OT1RFX0ZPUk1BVDtcbmV4cG9ydHMuREVGQVVMVF9NT05USExZX05PVEVfRk9STUFUID0gREVGQVVMVF9NT05USExZX05PVEVfRk9STUFUO1xuZXhwb3J0cy5ERUZBVUxUX1FVQVJURVJMWV9OT1RFX0ZPUk1BVCA9IERFRkFVTFRfUVVBUlRFUkxZX05PVEVfRk9STUFUO1xuZXhwb3J0cy5ERUZBVUxUX1dFRUtMWV9OT1RFX0ZPUk1BVCA9IERFRkFVTFRfV0VFS0xZX05PVEVfRk9STUFUO1xuZXhwb3J0cy5ERUZBVUxUX1lFQVJMWV9OT1RFX0ZPUk1BVCA9IERFRkFVTFRfWUVBUkxZX05PVEVfRk9STUFUO1xuZXhwb3J0cy5hcHBIYXNEYWlseU5vdGVzUGx1Z2luTG9hZGVkID0gYXBwSGFzRGFpbHlOb3Rlc1BsdWdpbkxvYWRlZDtcbmV4cG9ydHMuYXBwSGFzTW9udGhseU5vdGVzUGx1Z2luTG9hZGVkID0gYXBwSGFzTW9udGhseU5vdGVzUGx1Z2luTG9hZGVkO1xuZXhwb3J0cy5hcHBIYXNRdWFydGVybHlOb3Rlc1BsdWdpbkxvYWRlZCA9IGFwcEhhc1F1YXJ0ZXJseU5vdGVzUGx1Z2luTG9hZGVkO1xuZXhwb3J0cy5hcHBIYXNXZWVrbHlOb3Rlc1BsdWdpbkxvYWRlZCA9IGFwcEhhc1dlZWtseU5vdGVzUGx1Z2luTG9hZGVkO1xuZXhwb3J0cy5hcHBIYXNZZWFybHlOb3Rlc1BsdWdpbkxvYWRlZCA9IGFwcEhhc1llYXJseU5vdGVzUGx1Z2luTG9hZGVkO1xuZXhwb3J0cy5jcmVhdGVEYWlseU5vdGUgPSBjcmVhdGVEYWlseU5vdGU7XG5leHBvcnRzLmNyZWF0ZU1vbnRobHlOb3RlID0gY3JlYXRlTW9udGhseU5vdGU7XG5leHBvcnRzLmNyZWF0ZVBlcmlvZGljTm90ZSA9IGNyZWF0ZVBlcmlvZGljTm90ZTtcbmV4cG9ydHMuY3JlYXRlUXVhcnRlcmx5Tm90ZSA9IGNyZWF0ZVF1YXJ0ZXJseU5vdGU7XG5leHBvcnRzLmNyZWF0ZVdlZWtseU5vdGUgPSBjcmVhdGVXZWVrbHlOb3RlO1xuZXhwb3J0cy5jcmVhdGVZZWFybHlOb3RlID0gY3JlYXRlWWVhcmx5Tm90ZTtcbmV4cG9ydHMuZ2V0QWxsRGFpbHlOb3RlcyA9IGdldEFsbERhaWx5Tm90ZXM7XG5leHBvcnRzLmdldEFsbE1vbnRobHlOb3RlcyA9IGdldEFsbE1vbnRobHlOb3RlcztcbmV4cG9ydHMuZ2V0QWxsUXVhcnRlcmx5Tm90ZXMgPSBnZXRBbGxRdWFydGVybHlOb3RlcztcbmV4cG9ydHMuZ2V0QWxsV2Vla2x5Tm90ZXMgPSBnZXRBbGxXZWVrbHlOb3RlcztcbmV4cG9ydHMuZ2V0QWxsWWVhcmx5Tm90ZXMgPSBnZXRBbGxZZWFybHlOb3RlcztcbmV4cG9ydHMuZ2V0RGFpbHlOb3RlID0gZ2V0RGFpbHlOb3RlO1xuZXhwb3J0cy5nZXREYWlseU5vdGVTZXR0aW5ncyA9IGdldERhaWx5Tm90ZVNldHRpbmdzO1xuZXhwb3J0cy5nZXREYXRlRnJvbUZpbGUgPSBnZXREYXRlRnJvbUZpbGU7XG5leHBvcnRzLmdldERhdGVGcm9tUGF0aCA9IGdldERhdGVGcm9tUGF0aDtcbmV4cG9ydHMuZ2V0RGF0ZVVJRCA9IGdldERhdGVVSUQ7XG5leHBvcnRzLmdldE1vbnRobHlOb3RlID0gZ2V0TW9udGhseU5vdGU7XG5leHBvcnRzLmdldE1vbnRobHlOb3RlU2V0dGluZ3MgPSBnZXRNb250aGx5Tm90ZVNldHRpbmdzO1xuZXhwb3J0cy5nZXRQZXJpb2RpY05vdGVTZXR0aW5ncyA9IGdldFBlcmlvZGljTm90ZVNldHRpbmdzO1xuZXhwb3J0cy5nZXRRdWFydGVybHlOb3RlID0gZ2V0UXVhcnRlcmx5Tm90ZTtcbmV4cG9ydHMuZ2V0UXVhcnRlcmx5Tm90ZVNldHRpbmdzID0gZ2V0UXVhcnRlcmx5Tm90ZVNldHRpbmdzO1xuZXhwb3J0cy5nZXRUZW1wbGF0ZUluZm8gPSBnZXRUZW1wbGF0ZUluZm87XG5leHBvcnRzLmdldFdlZWtseU5vdGUgPSBnZXRXZWVrbHlOb3RlO1xuZXhwb3J0cy5nZXRXZWVrbHlOb3RlU2V0dGluZ3MgPSBnZXRXZWVrbHlOb3RlU2V0dGluZ3M7XG5leHBvcnRzLmdldFllYXJseU5vdGUgPSBnZXRZZWFybHlOb3RlO1xuZXhwb3J0cy5nZXRZZWFybHlOb3RlU2V0dGluZ3MgPSBnZXRZZWFybHlOb3RlU2V0dGluZ3M7XG4iLCAiaW1wb3J0IHsgUGx1Z2luIH0gZnJvbSBcIm9ic2lkaWFuXCI7XG5pbXBvcnQgeyBCcmF0U2V0dGluZ3NUYWIgfSBmcm9tIFwiLi91aS9TZXR0aW5nc1RhYlwiO1xuaW1wb3J0IHsgU2V0dGluZ3MsIERFRkFVTFRfU0VUVElOR1MgfSBmcm9tIFwiLi91aS9zZXR0aW5nc1wiO1xuaW1wb3J0IEJldGFQbHVnaW5zIGZyb20gXCIuL2ZlYXR1cmVzL0JldGFQbHVnaW5zXCI7XG5pbXBvcnQgeyBhZGRJY29ucyB9IGZyb20gXCIuL3VpL2ljb25zXCI7XG5pbXBvcnQgeyBsb2dnZXIgfSBmcm9tIFwiLi91dGlscy9sb2dnaW5nXCI7XG5pbXBvcnQgUGx1Z2luQ29tbWFuZHMgZnJvbSBcIi4vdWkvUGx1Z2luQ29tbWFuZHNcIjtcbmltcG9ydCB7IHRoZW1lc0NoZWNrQW5kVXBkYXRlcyB9IGZyb20gXCIuL2ZlYXR1cmVzL3RoZW1lc1wiO1xuaW1wb3J0IEJyYXRBUEkgZnJvbSBcIi4vdXRpbHMvQnJhdEFQSVwiO1xuXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBUaGVQbHVnaW4gZXh0ZW5kcyBQbHVnaW4ge1xuXHRhcHBOYW1lID0gXCJPYnNpZGlhbjQyIC0gQmV0YSBSZXZpZXdlcidzIEF1dG8tdXBkYXRlIFRvb2wgKEJSQVQpXCI7XG5cdGFwcElEID0gXCJvYnNpZGlhbjQyLWJyYXRcIjtcblx0c2V0dGluZ3M6IFNldHRpbmdzO1xuXHRiZXRhUGx1Z2luczogQmV0YVBsdWdpbnM7XG5cdHJpYmJvbkljb246IEhUTUxFbGVtZW50O1xuXHRjb21tYW5kczogUGx1Z2luQ29tbWFuZHM7XG5cdGJyYXRBUEk6IEJyYXRBUElcblxuXHRhc3luYyBvbmxvYWQoKTogUHJvbWlzZTx2b2lkPiB7XG5cdFx0Y29uc29sZS5sb2coXCJsb2FkaW5nIE9ic2lkaWFuNDIgLSBCUkFUXCIpO1x0XHRcblxuXHRcdGF3YWl0IHRoaXMubG9hZFNldHRpbmdzKCk7XG5cdFx0dGhpcy5hZGRTZXR0aW5nVGFiKG5ldyBCcmF0U2V0dGluZ3NUYWIodGhpcy5hcHAsIHRoaXMpKTtcblxuXHRcdHRoaXMuYmV0YVBsdWdpbnMgPSBuZXcgQmV0YVBsdWdpbnModGhpcyk7XG5cdFx0dGhpcy5jb21tYW5kcyA9IG5ldyBQbHVnaW5Db21tYW5kcyh0aGlzKTtcblxuXHRcdGFkZEljb25zKCk7XG5cdFx0aWYgKHRoaXMuc2V0dGluZ3MucmliYm9uSWNvbkVuYWJsZWQpIHRoaXMuc2hvd1JpYmJvbkJ1dHRvbigpO1xuXG5cdFx0dGhpcy5hcHAud29ya3NwYWNlLm9uTGF5b3V0UmVhZHkoKCk6IHZvaWQgPT4geyAvLyBsZXQgb2JzaWRpYW4gbG9hZCBhbmQgY2FsbSBkb3duIGJlZm9yZSBjaGVja1xuXHRcdFx0aWYgKHRoaXMuc2V0dGluZ3MudXBkYXRlQXRTdGFydHVwKSB7IFxuXHRcdFx0XHRzZXRUaW1lb3V0KGFzeW5jICgpID0+IHtcblx0XHRcdFx0XHRhd2FpdCB0aGlzLmJldGFQbHVnaW5zLmNoZWNrRm9yVXBkYXRlc0FuZEluc3RhbGxVcGRhdGVzKGZhbHNlKVxuXHRcdFx0XHR9LCA2MDAwMCk7XG5cdFx0XHR9XG5cdFx0XHRpZiAodGhpcy5zZXR0aW5ncy51cGRhdGVUaGVtZXNBdFN0YXJ0dXApIHsgXG5cdFx0XHRcdHNldFRpbWVvdXQoYXN5bmMgKCkgPT4ge1xuXHRcdFx0XHRcdGF3YWl0IHRoZW1lc0NoZWNrQW5kVXBkYXRlcyh0aGlzLCBmYWxzZSk7XG5cdFx0XHRcdH0sIDEyMDAwMCk7XG5cdFx0XHR9XG5cdFx0XHRzZXRUaW1lb3V0KGFzeW5jICgpID0+IHtcblx0XHRcdFx0dGhpcy5icmF0QVBJID0gbmV3IEJyYXRBUEkodGhpcyk7XG5cdFx0XHRcdChnbG9iYWxUaGlzIGFzIGFueSkuYnJhdEFQSSA9IHRoaXMuYnJhdEFQSTtcblx0XHRcdH0sIDUwMCk7XG5cdFx0fSk7XG5cdH1cblx0c2hvd1JpYmJvbkJ1dHRvbigpOiB2b2lkIHsgdGhpcy5yaWJib25JY29uID0gdGhpcy5hZGRSaWJib25JY29uKFwiQnJhdEljb25cIiwgXCJCUkFUXCIsIGFzeW5jICgpID0+IHRoaXMuY29tbWFuZHMucmliYm9uRGlzcGxheUNvbW1hbmRzKCkpIH1cblxuXHRsb2codGV4dFRvTG9nOiBzdHJpbmcsIHZlcmJvc2UgPSBmYWxzZSk6IHZvaWQgeyBsb2dnZXIodGhpcywgdGV4dFRvTG9nLCB2ZXJib3NlKSB9XG5cdFxuXHRvbnVubG9hZCgpOiB2b2lkIHsgY29uc29sZS5sb2coXCJ1bmxvYWRpbmcgXCIgKyB0aGlzLmFwcE5hbWUpIH1cblxuXHRhc3luYyBsb2FkU2V0dGluZ3MoKTogUHJvbWlzZTx2b2lkPiB7IHRoaXMuc2V0dGluZ3MgPSBPYmplY3QuYXNzaWduKHt9LCBERUZBVUxUX1NFVFRJTkdTLCBhd2FpdCB0aGlzLmxvYWREYXRhKCkpIH1cblxuXHRhc3luYyBzYXZlU2V0dGluZ3MoKTogUHJvbWlzZTx2b2lkPiB7IGF3YWl0IHRoaXMuc2F2ZURhdGEodGhpcy5zZXR0aW5ncykgfVxufSIsICJpbXBvcnQgeyBBcHAsIFBsdWdpblNldHRpbmdUYWIsIFNldHRpbmcsIFRvZ2dsZUNvbXBvbmVudCwgQnV0dG9uQ29tcG9uZW50IH0gZnJvbSAnb2JzaWRpYW4nO1xuaW1wb3J0IHsgdGhlbWVEZWxldGUgfSBmcm9tICcuLi9mZWF0dXJlcy90aGVtZXMnO1xuaW1wb3J0IFRoZVBsdWdpbiBmcm9tICcuLi9tYWluJztcbmltcG9ydCBBZGROZXdUaGVtZSBmcm9tICcuL0FkZE5ld1RoZW1lJztcbmltcG9ydCB7IHByb21vdGlvbmFsTGlua3MgfSBmcm9tICcuL1Byb21vdGlvbmFsJztcblxuZXhwb3J0IGNsYXNzIEJyYXRTZXR0aW5nc1RhYiBleHRlbmRzIFBsdWdpblNldHRpbmdUYWIge1xuXHRwbHVnaW46IFRoZVBsdWdpbjtcblxuXHRjb25zdHJ1Y3RvcihhcHA6IEFwcCwgcGx1Z2luOiBUaGVQbHVnaW4pIHtcblx0XHRzdXBlcihhcHAsIHBsdWdpbik7XG5cdFx0dGhpcy5wbHVnaW4gPSBwbHVnaW47XG5cdH1cblxuXHRkaXNwbGF5KCk6IHZvaWQge1xuXHRcdGNvbnN0IHsgY29udGFpbmVyRWwgfSA9IHRoaXM7XG5cdFx0Y29udGFpbmVyRWwuZW1wdHkoKTtcblxuXHRcdHByb21vdGlvbmFsTGlua3MoY29udGFpbmVyRWwsIHRydWUpXG5cblx0XHRjb250YWluZXJFbC5jcmVhdGVFbCgnaDEnLCB7IHRleHQ6IHRoaXMucGx1Z2luLmFwcE5hbWUgfSkgXG5cdFx0Ly8gLnN0eWxlLm1hcmdpblRvcCA9IFwiNTBweFwiO1xuXHRcdGNvbnRhaW5lckVsLmNyZWF0ZUVsKCdoMicsIHsgdGV4dDogXCJieSBUZlRIYWNrZXJcIiB9KSBcblxuXHRcdG5ldyBTZXR0aW5nKGNvbnRhaW5lckVsKVxuXHRcdFx0LnNldE5hbWUoJ0F1dG8tdXBkYXRlIHBsdWdpbnMgYXQgc3RhcnR1cCcpXG5cdFx0XHQuc2V0RGVzYygnSWYgZW5hYmxlZCBhbGwgYmV0YSBwbHVnaW5zIHdpbGwgYmUgY2hlY2tlZCBmb3IgdXBkYXRlcyBlYWNoIHRpbWUgT2JzaWRpYW4gc3RhcnRzLiBOb3RlOiB0aGlzIGRvZXMgbm90IHVwZGF0ZSBmcm96ZW4gdmVyc2lvbiBwbHVnaW5zLicpXG5cdFx0XHQuYWRkVG9nZ2xlKChjYjogVG9nZ2xlQ29tcG9uZW50KSA9PiB7XG5cdFx0XHRcdGNiLnNldFZhbHVlKHRoaXMucGx1Z2luLnNldHRpbmdzLnVwZGF0ZUF0U3RhcnR1cCk7XG5cdFx0XHRcdGNiLm9uQ2hhbmdlKGFzeW5jICh2YWx1ZTogYm9vbGVhbikgPT4ge1xuXHRcdFx0XHRcdHRoaXMucGx1Z2luLnNldHRpbmdzLnVwZGF0ZUF0U3RhcnR1cCA9IHZhbHVlO1xuXHRcdFx0XHRcdGF3YWl0IHRoaXMucGx1Z2luLnNhdmVTZXR0aW5ncygpO1xuXHRcdFx0XHR9KTtcblx0XHRcdH0pXG5cblx0XHRuZXcgU2V0dGluZyhjb250YWluZXJFbClcblx0XHRcdC5zZXROYW1lKCdBdXRvLXVwZGF0ZSB0aGVtZXMgYXQgc3RhcnR1cCcpXG5cdFx0XHQuc2V0RGVzYygnSWYgZW5hYmxlZCBhbGwgYmV0YSB0aGVtZXMgd2lsbCBiZSBjaGVja2VkIGZvciB1cGRhdGVzIGVhY2ggdGltZSBPYnNpZGlhbiBzdGFydHMuJylcblx0XHRcdC5hZGRUb2dnbGUoKGNiOiBUb2dnbGVDb21wb25lbnQpID0+IHtcblx0XHRcdFx0Y2Iuc2V0VmFsdWUodGhpcy5wbHVnaW4uc2V0dGluZ3MudXBkYXRlVGhlbWVzQXRTdGFydHVwKTtcblx0XHRcdFx0Y2Iub25DaGFuZ2UoYXN5bmMgKHZhbHVlOiBib29sZWFuKSA9PiB7XG5cdFx0XHRcdFx0dGhpcy5wbHVnaW4uc2V0dGluZ3MudXBkYXRlVGhlbWVzQXRTdGFydHVwID0gdmFsdWU7XG5cdFx0XHRcdFx0YXdhaXQgdGhpcy5wbHVnaW4uc2F2ZVNldHRpbmdzKCk7XG5cdFx0XHRcdH0pO1xuXHRcdFx0fSlcblxuXG5cdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXG5cdFx0XHQuc2V0TmFtZSgnUmliYm9uIEJ1dHRvbicpXG5cdFx0XHQuc2V0RGVzYygnVG9nZ2xlIHJpYmJvbiBidXR0b24gb2ZmIGFuZCBvbi4nKVxuXHRcdFx0LmFkZFRvZ2dsZSgoY2I6IFRvZ2dsZUNvbXBvbmVudCkgPT4ge1xuXHRcdFx0XHRjYi5zZXRWYWx1ZSh0aGlzLnBsdWdpbi5zZXR0aW5ncy5yaWJib25JY29uRW5hYmxlZCk7XG5cdFx0XHRcdGNiLm9uQ2hhbmdlKGFzeW5jICh2YWx1ZTogYm9vbGVhbikgPT4ge1xuXHRcdFx0XHRcdHRoaXMucGx1Z2luLnNldHRpbmdzLnJpYmJvbkljb25FbmFibGVkID0gdmFsdWU7XG5cdFx0XHRcdFx0aWYgKHRoaXMucGx1Z2luLnNldHRpbmdzLnJpYmJvbkljb25FbmFibGVkID09PSBmYWxzZSlcblx0XHRcdFx0XHRcdHRoaXMucGx1Z2luLnJpYmJvbkljb24ucmVtb3ZlKCk7XG5cdFx0XHRcdFx0ZWxzZVxuXHRcdFx0XHRcdFx0dGhpcy5wbHVnaW4uc2hvd1JpYmJvbkJ1dHRvbigpO1xuXHRcdFx0XHRcdGF3YWl0IHRoaXMucGx1Z2luLnNhdmVTZXR0aW5ncygpO1xuXHRcdFx0XHR9KTtcblx0XHRcdH0pXHRcdFx0XG5cblx0XHRjb250YWluZXJFbC5jcmVhdGVFbChcImhyXCIpO1xuXHRcdGNvbnRhaW5lckVsLmNyZWF0ZUVsKFwiaDJcIiwgeyB0ZXh0OiBcIkJldGEgUGx1Z2luIExpc3RcIiB9KTtcblx0XHRjb250YWluZXJFbC5jcmVhdGVFbChcImRpdlwiLCB7IHRleHQ6IGBUaGUgZm9sbG93aW5nIGlzIGEgbGlzdCBvZiBiZXRhIHBsdWdpbnMgYWRkZWQgdmlhIHRoZSBjb21tYW5kIHBhbGV0dGUgXCJBZGQgYSBiZXRhIHBsdWdpbiBmb3IgdGVzdGluZ1wiIG9yIFwiQWRkIGEgYmV0YSBwbHVnaW4gd2l0aCBmcm96ZW4gdmVyc2lvbiBmb3IgdGVzdGluZ1wiLiBBIGZyb3plbiB2ZXJzaW9uIGlzIGEgc3BlY2lmaWMgcmVsZWFzZSBvZiBhIHBsdWdpbiBiYXNlZCBvbiBpdHMgcmVsZWVhc2UgdGFnLiBgIH0pO1xuXHRcdGNvbnRhaW5lckVsLmNyZWF0ZUVsKFwicFwiKTtcblx0XHRjb250YWluZXJFbC5jcmVhdGVFbChcImRpdlwiLCB7IHRleHQ6IGBDbGljayB0aGUgeCBidXR0b24gbmV4dCB0byBhIHBsdWdpbiB0byByZW1vdmUgaXQgZnJvbSB0aGUgbGlzdC5gIH0pO1xuXHRcdGNvbnRhaW5lckVsLmNyZWF0ZUVsKFwicFwiKTtcblx0XHRjb250YWluZXJFbC5jcmVhdGVFbChcInNwYW5cIilcblx0XHRcdC5jcmVhdGVFbChcImJcIiwgeyB0ZXh0OiBcIk5vdGU6IFwiIH0pXG5cdFx0Y29udGFpbmVyRWwuY3JlYXRlU3Bhbih7IHRleHQ6IFwiVGhpcyBkb2VzIG5vdCBkZWxldGUgdGhlIHBsdWdpbiwgdGhpcyBzaG91bGQgYmUgZG9uZSBmcm9tIHRoZSAgQ29tbXVuaXR5IFBsdWdpbnMgdGFiIGluIFNldHRpbmdzLlwiIH0pO1xuXG5cdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXG5cdFx0XHQuYWRkQnV0dG9uKChjYjogQnV0dG9uQ29tcG9uZW50KT0+e1xuXHRcdFx0XHRjYi5zZXRCdXR0b25UZXh0KFwiQWRkIEJldGEgcGx1Z2luXCIpXG5cdFx0XHRcdGNiLm9uQ2xpY2soYXN5bmMgKCk9Pntcblx0XHRcdFx0XHQvLyBAdHMtaWdub3JlXG5cdFx0XHRcdFx0dGhpcy5wbHVnaW4uYXBwLnNldHRpbmcuY2xvc2UoKTtcblx0XHRcdFx0XHRhd2FpdCB0aGlzLnBsdWdpbi5iZXRhUGx1Z2lucy5kaXNwbGF5QWRkTmV3UGx1Z2luTW9kYWwodHJ1ZSwgZmFsc2UpO1xuXHRcdFx0XHR9KVxuXHRcdFx0fSk7XG5cblx0XHRjb25zdCBwbHVnaW5TdWJMaXN0RnJvemVuVmVyc2lvbk5hbWVzXG5cdFx0XHQ9IG5ldyBTZXQodGhpcy5wbHVnaW4uc2V0dGluZ3MucGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb24ubWFwKHggPT4geC5yZXBvKSk7XG5cdFx0Zm9yIChjb25zdCBicCBvZiB0aGlzLnBsdWdpbi5zZXR0aW5ncy5wbHVnaW5MaXN0KSB7XG5cdFx0XHRpZiAocGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb25OYW1lcy5oYXMoYnApKSB7XG5cdFx0XHRcdGNvbnRpbnVlO1xuXHRcdFx0fVxuXHRcdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXG5cdFx0XHRcdC5zZXROYW1lKGJwKVxuXHRcdFx0XHQuYWRkQnV0dG9uKChidG46IEJ1dHRvbkNvbXBvbmVudCkgPT4ge1xuXHRcdFx0XHRcdGJ0bi5zZXRJY29uKFwiY3Jvc3NcIik7XG5cdFx0XHRcdFx0YnRuLnNldFRvb2x0aXAoXCJEZWxldGUgdGhpcyBiZXRhIHBsdWdpblwiKTtcblx0XHRcdFx0XHRidG4ub25DbGljayhhc3luYyAoKSA9PiB7XG5cdFx0XHRcdFx0XHQvLyBhd2FpdCB0aGlzLnBsdWdpbi5iZXRhUGx1Z2lucy5kZWxldGVQbHVnaW4oYnApO1xuXHRcdFx0XHRcdFx0aWYgKGJ0bi5idXR0b25FbC50ZXh0Q29udGVudCA9PT0gXCJcIilcblx0XHRcdFx0XHRcdFx0YnRuLnNldEJ1dHRvblRleHQoXCJDbGljayBvbmNlIG1vcmUgdG8gY29uZmlybSByZW1vdmFsXCIpO1xuXHRcdFx0XHRcdFx0ZWxzZSB7XG5cdFx0XHRcdFx0XHRcdGJ0bi5idXR0b25FbC5wYXJlbnRFbGVtZW50IS5wYXJlbnRFbGVtZW50IS5yZW1vdmUoKTtcblx0XHRcdFx0XHRcdFx0YXdhaXQgdGhpcy5wbHVnaW4uYmV0YVBsdWdpbnMuZGVsZXRlUGx1Z2luKGJwKVxuXHRcdFx0XHRcdFx0fVxuXHRcdFx0XHRcdH0pO1xuXHRcdFx0XHR9KVxuXHRcdH1cblxuXHRcdG5ldyBTZXR0aW5nKGNvbnRhaW5lckVsKVxuXHRcdFx0LmFkZEJ1dHRvbigoY2I6IEJ1dHRvbkNvbXBvbmVudCk9Pntcblx0XHRcdFx0Y2Iuc2V0QnV0dG9uVGV4dChcIkFkZCBCZXRhIHBsdWdpbiB3aXRoIGZyb3plbiB2ZXJzaW9uXCIpXG5cdFx0XHRcdGNiLm9uQ2xpY2soYXN5bmMgKCk9Pntcblx0XHRcdFx0XHQvLyBAdHMtaWdub3JlXG5cdFx0XHRcdFx0dGhpcy5wbHVnaW4uYXBwLnNldHRpbmcuY2xvc2UoKTtcblx0XHRcdFx0XHRhd2FpdCB0aGlzLnBsdWdpbi5iZXRhUGx1Z2lucy5kaXNwbGF5QWRkTmV3UGx1Z2luTW9kYWwodHJ1ZSwgdHJ1ZSk7XG5cdFx0XHRcdH0pXG5cdFx0XHR9KTtcblx0XHRmb3IgKGNvbnN0IGJwIG9mIHRoaXMucGx1Z2luLnNldHRpbmdzLnBsdWdpblN1Ykxpc3RGcm96ZW5WZXJzaW9uKSB7XG5cdFx0XHRuZXcgU2V0dGluZyhjb250YWluZXJFbClcblx0XHRcdFx0LnNldE5hbWUoYCR7YnAucmVwb30gKHZlcnNpb24gJHticC52ZXJzaW9ufSlgKVxuXHRcdFx0XHQuYWRkQnV0dG9uKChidG46IEJ1dHRvbkNvbXBvbmVudCkgPT4ge1xuXHRcdFx0XHRcdGJ0bi5zZXRJY29uKFwiY3Jvc3NcIik7XG5cdFx0XHRcdFx0YnRuLnNldFRvb2x0aXAoXCJEZWxldGUgdGhpcyBiZXRhIHBsdWdpblwiKTtcblx0XHRcdFx0XHRidG4ub25DbGljayhhc3luYyAoKSA9PiB7XG5cdFx0XHRcdFx0XHQvLyBhd2FpdCB0aGlzLnBsdWdpbi5iZXRhUGx1Z2lucy5kZWxldGVQbHVnaW4oYnApO1xuXHRcdFx0XHRcdFx0aWYgKGJ0bi5idXR0b25FbC50ZXh0Q29udGVudCA9PT0gXCJcIilcblx0XHRcdFx0XHRcdFx0YnRuLnNldEJ1dHRvblRleHQoXCJDbGljayBvbmNlIG1vcmUgdG8gY29uZmlybSByZW1vdmFsXCIpO1xuXHRcdFx0XHRcdFx0ZWxzZSB7XG5cdFx0XHRcdFx0XHRcdGJ0bi5idXR0b25FbC5wYXJlbnRFbGVtZW50IS5wYXJlbnRFbGVtZW50IS5yZW1vdmUoKTtcblx0XHRcdFx0XHRcdFx0YXdhaXQgdGhpcy5wbHVnaW4uYmV0YVBsdWdpbnMuZGVsZXRlUGx1Z2luKGJwLnJlcG8pO1xuXHRcdFx0XHRcdFx0fVxuXHRcdFx0XHRcdH0pO1xuXHRcdFx0XHR9KVxuXHRcdH1cblxuXHRcdGNvbnRhaW5lckVsLmNyZWF0ZUVsKFwiaHJcIik7XG5cdFx0Y29udGFpbmVyRWwuY3JlYXRlRWwoXCJoMlwiLCB7IHRleHQ6IFwiQmV0YSBUaGVtZXMgTGlzdFwiIH0pO1xuXG5cdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXG5cdFx0XHQuYWRkQnV0dG9uKChjYjogQnV0dG9uQ29tcG9uZW50KT0+e1xuXHRcdFx0XHRjYi5zZXRCdXR0b25UZXh0KFwiQWRkIEJldGEgVGhlbWVcIilcblx0XHRcdFx0Y2Iub25DbGljayhhc3luYyAoKT0+e1xuXHRcdFx0XHRcdC8vIEB0cy1pZ25vcmVcblx0XHRcdFx0XHR0aGlzLnBsdWdpbi5hcHAuc2V0dGluZy5jbG9zZSgpO1xuXHRcdFx0XHRcdChuZXcgQWRkTmV3VGhlbWUodGhpcy5wbHVnaW4pKS5vcGVuKCk7XG5cdFx0XHRcdH0pXG5cdFx0XHR9KTtcdFx0XG5cblxuXHRcdGZvciAoY29uc3QgYnAgb2YgdGhpcy5wbHVnaW4uc2V0dGluZ3MudGhlbWVzTGlzdCkge1xuXHRcdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXG5cdFx0XHRcdC5zZXROYW1lKGJwLnJlcG8pXG5cdFx0XHRcdC5hZGRCdXR0b24oKGJ0bjogQnV0dG9uQ29tcG9uZW50KSA9PiB7XG5cdFx0XHRcdFx0YnRuLnNldEljb24oXCJjcm9zc1wiKTtcblx0XHRcdFx0XHRidG4uc2V0VG9vbHRpcChcIkRlbGV0ZSB0aGlzIGJldGEgdGhlbWVcIik7XG5cdFx0XHRcdFx0YnRuLm9uQ2xpY2soYXN5bmMgKCkgPT4ge1xuXHRcdFx0XHRcdFx0aWYgKGJ0bi5idXR0b25FbC50ZXh0Q29udGVudCA9PT0gXCJcIilcblx0XHRcdFx0XHRcdFx0YnRuLnNldEJ1dHRvblRleHQoXCJDbGljayBvbmNlIG1vcmUgdG8gY29uZmlybSByZW1vdmFsXCIpO1xuXHRcdFx0XHRcdFx0ZWxzZSB7XG5cdFx0XHRcdFx0XHRcdGJ0bi5idXR0b25FbC5wYXJlbnRFbGVtZW50IS5wYXJlbnRFbGVtZW50IS5yZW1vdmUoKTtcblx0XHRcdFx0XHRcdFx0YXdhaXQgdGhlbWVEZWxldGUodGhpcy5wbHVnaW4sIGJwLnJlcG8pO1xuXHRcdFx0XHRcdFx0fVxuXHRcdFx0XHRcdH0pO1xuXHRcdFx0XHR9KVxuXHRcdH1cblxuXHRcdGNvbnRhaW5lckVsLmNyZWF0ZUVsKFwiaHJcIik7XG5cdFx0Y29udGFpbmVyRWwuY3JlYXRlRWwoXCJoMlwiLCB7IHRleHQ6IFwiTW9uaXRvcmluZ1wiIH0pO1xuXG5cdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXG5cdFx0XHQuc2V0TmFtZSgnRW5hYmxlIE5vdGlmaWNhdGlvbnMnKVxuXHRcdFx0LnNldERlc2MoJ0JSQVQgd2lsbCBwcm92aWRlIHBvcHVwIG5vdGlmaWNhdGlvbnMgZm9yIGl0cyB2YXJpb3VzIGFjdGl2aXRpZXMuIFR1cm4gdGhpcyBvZmYgbWVhbnMgIG5vIG5vdGlmaWNhdGlvbnMgZnJvbSBCUkFULicpXG5cdFx0XHQuYWRkVG9nZ2xlKChjYjogVG9nZ2xlQ29tcG9uZW50KSA9PiB7XG5cdFx0XHRcdGNiLnNldFZhbHVlKHRoaXMucGx1Z2luLnNldHRpbmdzLm5vdGlmaWNhdGlvbnNFbmFibGVkKTtcblx0XHRcdFx0Y2Iub25DaGFuZ2UoYXN5bmMgKHZhbHVlOiBib29sZWFuKSA9PiB7XG5cdFx0XHRcdFx0dGhpcy5wbHVnaW4uc2V0dGluZ3Mubm90aWZpY2F0aW9uc0VuYWJsZWQgPSB2YWx1ZTtcblx0XHRcdFx0XHRhd2FpdCB0aGlzLnBsdWdpbi5zYXZlU2V0dGluZ3MoKTtcblx0XHRcdFx0fSk7XG5cdFx0XHR9KVxuXG5cdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXG5cdFx0XHQuc2V0TmFtZSgnRW5hYmxlIExvZ2dpbmcnKVxuXHRcdFx0LnNldERlc2MoJ1BsdWdpbiB1cGRhdGVzIHdpbGwgYmUgbG9nZ2VkIHRvIGEgZmlsZSBpbiB0aGUgbG9nIGZpbGUuJylcblx0XHRcdC5hZGRUb2dnbGUoKGNiOiBUb2dnbGVDb21wb25lbnQpID0+IHtcblx0XHRcdFx0Y2Iuc2V0VmFsdWUodGhpcy5wbHVnaW4uc2V0dGluZ3MubG9nZ2luZ0VuYWJsZWQpO1xuXHRcdFx0XHRjYi5vbkNoYW5nZShhc3luYyAodmFsdWU6IGJvb2xlYW4pID0+IHtcblx0XHRcdFx0XHR0aGlzLnBsdWdpbi5zZXR0aW5ncy5sb2dnaW5nRW5hYmxlZCA9IHZhbHVlO1xuXHRcdFx0XHRcdGF3YWl0IHRoaXMucGx1Z2luLnNhdmVTZXR0aW5ncygpO1xuXHRcdFx0XHR9KTtcblx0XHRcdH0pXG5cblx0XHRuZXcgU2V0dGluZyh0aGlzLmNvbnRhaW5lckVsKVxuICAgICAgICAgICAgLnNldE5hbWUoXCJCUkFUIExvZyBGaWxlIExvY2F0aW9uXCIpXG4gICAgICAgICAgICAuc2V0RGVzYyhcIkxvZ3Mgd2lsbCBiZSBzYXZlZCB0byB0aGlzIGZpbGUuIERvbid0IGFkZCAubWQgdG8gdGhlIGZpbGUgbmFtZS5cIilcbiAgICAgICAgICAgIC5hZGRTZWFyY2goKGNiKSA9PiB7XG4gICAgICAgICAgICAgICAgY2Iuc2V0UGxhY2Vob2xkZXIoXCJFeGFtcGxlOiBCUkFULWxvZ1wiKVxuICAgICAgICAgICAgICAgICAgICAuc2V0VmFsdWUodGhpcy5wbHVnaW4uc2V0dGluZ3MubG9nZ2luZ1BhdGgpXG4gICAgICAgICAgICAgICAgICAgIC5vbkNoYW5nZShhc3luYyAobmV3X2ZvbGRlcikgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgdGhpcy5wbHVnaW4uc2V0dGluZ3MubG9nZ2luZ1BhdGggPSBuZXdfZm9sZGVyO1xuXHRcdFx0XHRcdFx0YXdhaXQgdGhpcy5wbHVnaW4uc2F2ZVNldHRpbmdzKCk7XG4gICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfSk7XHRcdFxuXG5cdFx0bmV3IFNldHRpbmcoY29udGFpbmVyRWwpXG5cdFx0XHQuc2V0TmFtZSgnRW5hYmxlIFZlcmJvc2UgTG9nZ2luZycpXG5cdFx0XHQuc2V0RGVzYygnR2V0IGEgbG90ICBtb3JlIGluZm9ybWF0aW9uIGluICB0aGUgbG9nLicpXG5cdFx0XHQuYWRkVG9nZ2xlKChjYjogVG9nZ2xlQ29tcG9uZW50KSA9PiB7XG5cdFx0XHRcdGNiLnNldFZhbHVlKHRoaXMucGx1Z2luLnNldHRpbmdzLmxvZ2dpbmdWZXJib3NlRW5hYmxlZCk7XG5cdFx0XHRcdGNiLm9uQ2hhbmdlKGFzeW5jICh2YWx1ZTogYm9vbGVhbikgPT4ge1xuXHRcdFx0XHRcdHRoaXMucGx1Z2luLnNldHRpbmdzLmxvZ2dpbmdWZXJib3NlRW5hYmxlZCA9IHZhbHVlO1xuXHRcdFx0XHRcdGF3YWl0IHRoaXMucGx1Z2luLnNhdmVTZXR0aW5ncygpO1xuXHRcdFx0XHR9KTtcblx0XHRcdH0pXG5cblxuXHRcdG5ldyBTZXR0aW5nKGNvbnRhaW5lckVsKVxuXHRcdFx0LnNldE5hbWUoJ0RlYnVnZ2luZyBNb2RlJylcblx0XHRcdC5zZXREZXNjKCdBdG9taWMgQm9tYiBsZXZlbCBjb25zb2xlIGxvZ2dpbmcuIENhbiBiZSB1c2VkIGZvciB0cm91Ymxlc2hvdGluZyBhbmQgZGV2ZWxvcG1lbnQuJylcblx0XHRcdC5hZGRUb2dnbGUoKGNiOiBUb2dnbGVDb21wb25lbnQpID0+IHtcblx0XHRcdFx0Y2Iuc2V0VmFsdWUodGhpcy5wbHVnaW4uc2V0dGluZ3MuZGVidWdnaW5nTW9kZSk7XG5cdFx0XHRcdGNiLm9uQ2hhbmdlKGFzeW5jICh2YWx1ZTogYm9vbGVhbikgPT4ge1xuXHRcdFx0XHRcdHRoaXMucGx1Z2luLnNldHRpbmdzLmRlYnVnZ2luZ01vZGUgPSB2YWx1ZTtcblx0XHRcdFx0XHRhd2FpdCB0aGlzLnBsdWdpbi5zYXZlU2V0dGluZ3MoKTtcblx0XHRcdFx0fSk7XG5cdFx0XHR9KVx0XHRcdFxuXHRcblx0fVxufVxuIiwgImltcG9ydCB7IG5vcm1hbGl6ZVBhdGgsIE5vdGljZSB9IGZyb20gXCJvYnNpZGlhblwiO1xuaW1wb3J0IFRoZVBsdWdpbiBmcm9tIFwiLi4vbWFpblwiO1xuaW1wb3J0IHsgYWRkQmV0YVRoZW1lVG9MaXN0LCB1cGRhdGVCZXRhVGhlbWVMYXN0VXBkYXRlQ2hlY2tzdW0gfSBmcm9tIFwiLi4vdWkvc2V0dGluZ3NcIjtcbmltcG9ydCB7IGNoZWNrc3VtRm9yU3RyaW5nLCBncmFiQ2hlY2tzdW1PZlRoZW1lQ3NzRmlsZSwgZ3JhYkNvbW1tdW5pdHlUaGVtZUNzc0ZpbGUsIGdyYWJDb21tbXVuaXR5VGhlbWVNYW5pZmVzdEZpbGUgfSBmcm9tIFwiLi9naXRodWJVdGlsc1wiO1xuaW1wb3J0IHsgVG9hc3RNZXNzYWdlIH0gZnJvbSBcIi4uL3V0aWxzL25vdGlmaWNhdGlvbnNcIjtcbmltcG9ydCB7IGlzQ29ubmVjdGVkVG9JbnRlcm5ldCB9IGZyb20gXCIuLi91dGlscy9pbnRlcm5ldGNvbm5lY3Rpb25cIjtcblxuXG4vKipcbiAqIEluc3RhbGxzIG9yIHVwZGF0ZXMgYSB0aGVtZVxuICpcbiAqIEBwYXJhbSAgIHtUaGVQbHVnaW59ICAgICBwbHVnaW4gICAgICAgICAgICAgICBUaGVQbHVnaW5cbiAqIEBwYXJhbSAgIHtzdHJpbmd9ICAgICAgICBjc3NHaXRodWJSZXBvc2l0b3J5ICBUaGUgcmVwb3NpdG9yeSB3aXRoIHRoZSB0aGVtZVxuICogQHBhcmFtICAge2Jvb2xlYW59ICAgICAgIG5ld0luc3RhbGwgICAgICAgICAgIHRydWUgPSBOZXcgdGhlbWUgaW5zdGFsbCwgZmFsc2UgdXBkYXRlIHRoZSB0aGVtZVxuICpcbiAqIEByZXR1cm4gIHtQcm9taXNlPGJvb2xlYW4+fSAgICAgICAgICAgICAgICAgICB0cnVlIGZvciBzdWNjY2Vzc1xuICovXG5leHBvcnQgY29uc3QgdGhlbWVTYXZlID0gYXN5bmMgKHBsdWdpbjogVGhlUGx1Z2luLCBjc3NHaXRodWJSZXBvc2l0b3J5OiBzdHJpbmcsIG5ld0luc3RhbGw6IGJvb2xlYW4pOiBQcm9taXNlPGJvb2xlYW4+ID0+IHtcbiAgICBsZXQgdGhlbWVDU1MgPSBhd2FpdCBncmFiQ29tbW11bml0eVRoZW1lQ3NzRmlsZShjc3NHaXRodWJSZXBvc2l0b3J5LCB0cnVlLCBwbHVnaW4uc2V0dGluZ3MuZGVidWdnaW5nTW9kZSk7IC8vdGVzdCBmb3IgdGhlbWVzLWJldGEuY3NzXG4gICAgaWYoIXRoZW1lQ1NTKSB0aGVtZUNTUyA9IGF3YWl0IGdyYWJDb21tbXVuaXR5VGhlbWVDc3NGaWxlKGNzc0dpdGh1YlJlcG9zaXRvcnksIGZhbHNlLCBwbHVnaW4uc2V0dGluZ3MuZGVidWdnaW5nTW9kZSk7IC8vIGdyYWJlIHRoZW1lcy5jc3MgaWYgbm8gYmV0YVxuXG4gICAgaWYoIXRoZW1lQ1NTKSB7XG4gICAgICAgIFRvYXN0TWVzc2FnZShwbHVnaW4sXCJUaGVyZSBpcyBubyB0aGVtZS5jc3Mgb3IgdGhlbWUtYmV0YS5jc3MgZmlsZSBpbiB0aGUgcm9vdCBwYXRoIG9mIHRoaXMgcmVwb3NpdG9yeSwgc28gdGhlcmUgaXMgbm8gdGhlbWUgdG8gaW5zdGFsbC5cIilcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH1cblxuICAgIGNvbnN0IHRoZW1lTWFuaWZlc3QgPSBhd2FpdCBncmFiQ29tbW11bml0eVRoZW1lTWFuaWZlc3RGaWxlKGNzc0dpdGh1YlJlcG9zaXRvcnksIHBsdWdpbi5zZXR0aW5ncy5kZWJ1Z2dpbmdNb2RlKTtcbiAgICBpZighdGhlbWVNYW5pZmVzdCkge1xuICAgICAgICBUb2FzdE1lc3NhZ2UocGx1Z2luLFwiVGhlcmUgaXMgbm8gbWFuaWZlc3QuanNvbiBmaWxlIGluIHRoZSByb290IHBhdGggb2YgdGhpcyByZXBvc2l0b3J5LCBzbyB0aGVtZSBjYW5ub3QgYmUgaW5zdGFsbGVkLlwiKVxuICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgfVxuXG4gICAgY29uc3QgbWFuaWZlc3RJbmZvID0gYXdhaXQgSlNPTi5wYXJzZSh0aGVtZU1hbmlmZXN0KTtcblxuICAgIGNvbnN0IHRoZW1lVGFyZ2V0Rm9sZGVyUGF0aCA9IG5vcm1hbGl6ZVBhdGgodGhlbWVzUm9vdFBhdGgocGx1Z2luKSArIG1hbmlmZXN0SW5mby5uYW1lKTtcblxuICAgIGNvbnN0IGFkYXB0ZXIgPSBwbHVnaW4uYXBwLnZhdWx0LmFkYXB0ZXI7XG4gICAgaWYgKGF3YWl0IGFkYXB0ZXIuZXhpc3RzKHRoZW1lVGFyZ2V0Rm9sZGVyUGF0aCkgPT09IGZhbHNlKSBhd2FpdCBhZGFwdGVyLm1rZGlyKHRoZW1lVGFyZ2V0Rm9sZGVyUGF0aCk7XG5cbiAgICBhd2FpdCBhZGFwdGVyLndyaXRlKCBub3JtYWxpemVQYXRoKHRoZW1lVGFyZ2V0Rm9sZGVyUGF0aCArIFwiL3RoZW1lLmNzc1wiKSwgdGhlbWVDU1MpO1xuICAgIGF3YWl0IGFkYXB0ZXIud3JpdGUoIG5vcm1hbGl6ZVBhdGgodGhlbWVUYXJnZXRGb2xkZXJQYXRoICsgXCIvbWFuaWZlc3QuanNvblwiKSwgdGhlbWVNYW5pZmVzdCk7XG5cbiAgICB1cGRhdGVCZXRhVGhlbWVMYXN0VXBkYXRlQ2hlY2tzdW0ocGx1Z2luLCBjc3NHaXRodWJSZXBvc2l0b3J5LCBjaGVja3N1bUZvclN0cmluZyh0aGVtZUNTUykpXG5cbiAgICBsZXQgbXNnID0gYGA7XG4gICAgXG4gICAgaWYobmV3SW5zdGFsbCkge1xuICAgICAgICBhd2FpdCBhZGRCZXRhVGhlbWVUb0xpc3QocGx1Z2luLCBjc3NHaXRodWJSZXBvc2l0b3J5LCB0aGVtZUNTUyk7XG4gICAgICAgIG1zZyA9IGAke21hbmlmZXN0SW5mby5uYW1lfSB0aGVtZSBpbnN0YWxsZWQgZnJvbSAke2Nzc0dpdGh1YlJlcG9zaXRvcnl9LiBgO1xuICAgICAgICBzZXRUaW1lb3V0KCgpID0+IHtcbiAgICAgICAgICAgIC8vIEB0cy1pZ25vcmUgICAgICAgICAgICBcbiAgICAgICAgICAgIHBsdWdpbi5hcHAuY3VzdG9tQ3NzLnNldFRoZW1lKG1hbmlmZXN0SW5mby5uYW1lKTtcbiAgICAgICAgfSwgNTAwKTsgICAgXG4gICAgfSBlbHNlIHtcbiAgICAgICAgbXNnID0gYCR7bWFuaWZlc3RJbmZvLm5hbWV9IHRoZW1lIHVwZGF0ZWQgZnJvbSAke2Nzc0dpdGh1YlJlcG9zaXRvcnl9LmA7XG4gICAgfVxuXG4gICAgcGx1Z2luLmxvZyhtc2cgKyBgW1RoZW1lIEluZm9dKGh0dHBzOi8vZ2l0aHViLmNvbS8ke2Nzc0dpdGh1YlJlcG9zaXRvcnl9KWAsIGZhbHNlKTtcbiAgICBUb2FzdE1lc3NhZ2UocGx1Z2luLGAke21zZ31gLDIwLCBhc3luYyAoKTpQcm9taXNlPHZvaWQ+PT57IHdpbmRvdy5vcGVuKGBodHRwczovL2dpdGh1Yi5jb20vJHtjc3NHaXRodWJSZXBvc2l0b3J5fWApfSk7XG4gICAgcmV0dXJuIHRydWU7XG59XG5cbi8qKlxuICogQ2hlY2tzICBpZiB0aGVyZSAgYXJlIHRoZW1lIHVwZGF0ZXMgYmFzZWQgb24gdGhlIGNvbW1pdCBkYXRlIG9mIHRoZSBvYnNpZGlhbi5jc3MgZmlsZSBvbiBnaXRodWIgaW4gY29tcGFyaXNvbiB0byB3aGF0IGlzIHN0b3JlZCBpbiB0aGUgQlJBVCB0aGVtZSBsaXN0XG4gKlxuICogQHBhcmFtICAge1RoZVBsdWdpbn0gICAgICBwbHVnaW4gICAgVGhlUGx1Z2luXG4gKiBAcGFyYW0gICB7Ym9vbGVhbjx2b2lkPn0gIHNob3dJbmZvICBwcm92aWRlICBub3RpY2VzIGR1cmluZyB0aGUgdXBkYXRlIHByb2Nlc1xuICpcbiAqIEByZXR1cm4gIHtQcm9taXNlPHZvaWQ+fSAgICAgICAgICAgIFxuICovXG5leHBvcnQgY29uc3QgdGhlbWVzQ2hlY2tBbmRVcGRhdGVzID0gYXN5bmMgKHBsdWdpbjogVGhlUGx1Z2luLCBzaG93SW5mbzogYm9vbGVhbik6IFByb21pc2U8dm9pZD4gPT4ge1xuICAgIGlmKGF3YWl0IGlzQ29ubmVjdGVkVG9JbnRlcm5ldCgpPT09ZmFsc2UpIHsgXG4gICAgICAgIGNvbnNvbGUubG9nKFwiQlJBVDogTm8gaW50ZXJuZXQgZGV0ZWN0ZWQuXCIpIFxuICAgICAgICByZXR1cm47XG4gICAgfVxuICAgIGxldCBuZXdOb3RpY2U6IE5vdGljZTtcbiAgICBjb25zdCBtc2cxID0gYENoZWNraW5nIGZvciBiZXRhIHRoZW1lIHVwZGF0ZXMgU1RBUlRFRGA7XG4gICAgcGx1Z2luLmxvZyhtc2cxLCB0cnVlKTtcbiAgICBpZiAoc2hvd0luZm8gJiYgcGx1Z2luLnNldHRpbmdzLm5vdGlmaWNhdGlvbnNFbmFibGVkKSBuZXdOb3RpY2UgPSBuZXcgTm90aWNlKGBCUkFUXFxuJHttc2cxfWAsIDMwMDAwKTtcbiAgICBmb3IoY29uc3QgdCBvZiBwbHVnaW4uc2V0dGluZ3MudGhlbWVzTGlzdCkge1xuICAgICAgICAvLyBmaXJzdCB0ZXN0IHRvIHNlZSBpZiB0aGVtZS1iZXRhLmNzcyBleGlzdHNcbiAgICAgICAgbGV0IGxhc3RVcGRhdGVPbmxpbmUgPSBhd2FpdCBncmFiQ2hlY2tzdW1PZlRoZW1lQ3NzRmlsZSh0LnJlcG8sIHRydWUsIHBsdWdpbi5zZXR0aW5ncy5kZWJ1Z2dpbmdNb2RlKTtcbiAgICAgICAgLy8gaWYgdGhlbWUtYmV0YS5jc3MgZG9lcyBOT1QgZXhpc3QsIHRyeSB0byBnZXQgdGhlbWUuY3NzXG4gICAgICAgIGlmKGxhc3RVcGRhdGVPbmxpbmU9PT1cIjBcIikgbGFzdFVwZGF0ZU9ubGluZSA9IGF3YWl0IGdyYWJDaGVja3N1bU9mVGhlbWVDc3NGaWxlKHQucmVwbywgZmFsc2UsIHBsdWdpbi5zZXR0aW5ncy5kZWJ1Z2dpbmdNb2RlKTtcbiAgICAgICAgaWYobGFzdFVwZGF0ZU9ubGluZSE9PXQubGFzdFVwZGF0ZSkgXG4gICAgICAgICAgICBhd2FpdCB0aGVtZVNhdmUocGx1Z2luLHQucmVwbyxmYWxzZSlcbiAgICB9XG4gICAgY29uc3QgbXNnMiA9IGBDaGVja2luZyBmb3IgYmV0YSB0aGVtZSB1cGRhdGVzIENPTVBMRVRFRGA7XG4gICAgcGx1Z2luLmxvZyhtc2cyLCB0cnVlKTtcbiAgICBpZiAoc2hvd0luZm8pIHtcbiAgICAgICAgaWYocGx1Z2luLnNldHRpbmdzLm5vdGlmaWNhdGlvbnNFbmFibGVkKSBuZXdOb3RpY2UhLmhpZGUoKTtcbiAgICAgICAgVG9hc3RNZXNzYWdlKHBsdWdpbiwgbXNnMik7XG4gICAgfVxufSBcblxuLyoqXG4gKiBEZWxldGVzIGEgdGhlbWUgZnJvbSB0aGUgQlJBVCBsaXN0IChEb2VzIG5vdCBwaHlzaWNhbGx5IGRlbGV0ZSB0aGUgdGhlbWUpXG4gKlxuICogQHBhcmFtICAge1RoZVBsdWdpbn0gIHBsdWdpbiAgICAgICAgICAgICAgIFRoZVBsdWdpblxuICogQHBhcmFtICAge3N0cmluZ30gICAgIGNzc0dpdGh1YlJlcG9zaXRvcnkgIFJlcG9zaXRvcnkgcGF0aFxuICpcbiAqIEByZXR1cm4gIHt2b2lkfVxuICovXG5leHBvcnQgY29uc3QgdGhlbWVEZWxldGUgPSBhc3luYyAocGx1Z2luOiBUaGVQbHVnaW4sIGNzc0dpdGh1YlJlcG9zaXRvcnk6IHN0cmluZyk6IFByb21pc2U8dm9pZD4gPT4ge1xuICAgIHBsdWdpbi5zZXR0aW5ncy50aGVtZXNMaXN0ID0gcGx1Z2luLnNldHRpbmdzLnRoZW1lc0xpc3QuZmlsdGVyKCh0KSA9PiB0LnJlcG8gIT0gY3NzR2l0aHViUmVwb3NpdG9yeSk7XG4gICAgcGx1Z2luLnNhdmVTZXR0aW5ncygpO1xuICAgIGNvbnN0IG1zZyA9IGBSZW1vdmVkICR7Y3NzR2l0aHViUmVwb3NpdG9yeX0gZnJvbSBCUkFUIHRoZW1lcyBsaXN0IGFuZCB3aWxsIG5vIGxvbmdlciBiZSB1cGRhdGVkLiBIb3dldmVyLCB0aGUgdGhlbWUgZmlsZXMgc3RpbGwgZXhpc3QgaW4gdGhlIHZhdWx0LiBUbyByZW1vdmUgdGhlbSwgZ28gaW50byBTZXR0aW5ncyA+IEFwcGVhcmFuY2UgYW5kIHJlbW92ZSB0aGUgdGhlbWUuYDtcbiAgICBwbHVnaW4ubG9nKG1zZywgdHJ1ZSk7XG4gICAgVG9hc3RNZXNzYWdlKHBsdWdpbiwgYCR7bXNnfWApO1xufVxuXG5cbi8qKlxuICogR2V0IHRoZSBwYXRoIHRvIHRoZSB0aGVtZXMgZm9sZGVyIGZvIHJ0aGlzIHZhdWx0XG4gKlxuICogQHBhcmFtICAge1RoZVBsdWdpbn0gIHBsdWdpbiAgVGhQbHVnaW5cbiAqXG4gKiBAcmV0dXJuICB7c3RyaW5nfSAgICAgICAgICAgICBwYXRoIHRvIHRoZW1lcyBmb2xkZXJcbiAqL1xuZXhwb3J0IGNvbnN0IHRoZW1lc1Jvb3RQYXRoID0gKHBsdWdpbjogVGhlUGx1Z2luKTogc3RyaW5nID0+IHtcbiAgICByZXR1cm4gbm9ybWFsaXplUGF0aChwbHVnaW4uYXBwLnZhdWx0LmNvbmZpZ0RpciArIFwiL3RoZW1lc1wiKSArIFwiL1wiO1xufVxuXG4iLCAiaW1wb3J0IHsgUGx1Z2luTWFuaWZlc3QsIHJlcXVlc3QgfSBmcm9tIFwib2JzaWRpYW5cIjtcblxuY29uc3QgR0lUSFVCX1JBV19VU0VSQ09OVEVOVF9QQVRIID0gXCJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vXCI7XG5cbi8qKlxuICogcHVsbHMgZnJvbSBnaXRodWIgYSByZWxlYXNlIGZpbGUgYnkgaXRzIHZlcnNpb24gbnVtYmVyXG4gKlxuICogQHBhcmFtICAge3N0cmluZ30gICAgICAgICAgIHJlcG9zaXRvcnkgIHBhdGggdG8gR2l0SHViIHJlcG9zaXRvcnkgaW4gZm9ybWF0IFVTRVJOQU1FL3JlcG9zaXRvcnlcbiAqIEBwYXJhbSAgIHtzdHJpbmd9ICAgICAgICAgICB2ZXJzaW9uICAgICB2ZXJzaW9uIG9mIHJlbGVhc2UgdG8gcmV0cml2ZSBcbiAqIEBwYXJhbSAgIHtzdHJpbmc8c3RyaW5nPn0gICBmaWxlTmFtZSAgICBuYW1lIG9mIGZpbGUgdG8gcmV0cmlldmUgZnJvbSByZWxlYXNlXG4gKlxuICogQHJldHVybiAge1Byb21pc2U8c3RyaW5nPn0gICAgICAgICAgICAgIGNvbnRlbnRzIG9mIGZpbGUgYXMgc3RyaW5nIGZyb20gdGhlIHJlcG9zaXRvcnkncyByZWxlYXNlXG4gKi9cbmV4cG9ydCBjb25zdCBncmFiUmVsZWFzZUZpbGVGcm9tUmVwb3NpdG9yeSA9IGFzeW5jIChyZXBvc2l0b3J5OiBzdHJpbmcsIHZlcnNpb246IHN0cmluZywgZmlsZU5hbWU6IHN0cmluZywgZGVidWdMb2dnaW5nID0gdHJ1ZSk6IFByb21pc2U8c3RyaW5nfG51bGw+ID0+IHtcbiAgICBjb25zdCBVUkwgPSBgaHR0cHM6Ly9naXRodWIuY29tLyR7cmVwb3NpdG9yeX0vcmVsZWFzZXMvZG93bmxvYWQvJHt2ZXJzaW9ufS8ke2ZpbGVOYW1lfWA7XG4gICAgdHJ5IHtcbiAgICAgICAgY29uc3QgZG93bmxvYWQgPSBhd2FpdCByZXF1ZXN0KHsgdXJsOiBVUkwgfSk7XG4gICAgICAgIHJldHVybiAoKGRvd25sb2FkID09PSBcIk5vdCBGb3VuZFwiIHx8IGRvd25sb2FkID09PSBge1wiZXJyb3JcIjpcIk5vdCBGb3VuZFwifWApID8gbnVsbCA6IGRvd25sb2FkKTtcbiAgICB9IGNhdGNoIChlcnJvcikge1xuICAgICAgICBpZihkZWJ1Z0xvZ2dpbmcpIGNvbnNvbGUubG9nKFwiZXJyb3IgaW4gZ3JhYlJlbGVhc2VGaWxlRnJvbVJlcG9zaXRvcnlcIiwgVVJMLCBlcnJvcilcbiAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxufVxuIFxuLyoqXG4gKiBncmFicyB0aGUgbWFuaWZlc3QuanNvbiBmcm9tIHRoZSByZXBvc2l0b3J5LiByb290TWFuaWZlc3QgLSBpZiB0cnVlIGdyYWJzIG1hbmlmZXN0Lmpzb24gaWYgZmFsc2UgZ3JhYnMgbWFuaWZlc3QtYmV0YS5qc29uXG4gKlxuICogQHBhcmFtICAge3N0cmluZ30gICAgICAgICAgICAgICAgICAgICByZXBvc2l0b3J5UGF0aCAgcGF0aCB0byBHaXRIdWIgcmVwb3NpdG9yeSBpbiBmb3JtYXQgVVNFUk5BTUUvcmVwb3NpdG9yeVxuICogQHBhcmFtICAge1t0eXBlXX0gICAgICAgICAgICAgICAgICAgICByb290TWFuaWZlc3QgICAgaWYgdHJ1ZSBncmFicyBtYW5pZmVzdC5qc29uIGlmIGZhbHNlIGdyYWJzIG1hbmlmZXN0LWJldGEuanNvblxuICpcbiAqIEByZXR1cm4gIHtQcm9taXNlPFBsdWdpbk1hbmlmZXN0Pn0gICAgICAgICAgICAgICAgICAgIHJldHVybnMgbWFuaWZlc3QgZmlsZSBmb3IgIGEgcGx1Z2luXG4gKi9cbmV4cG9ydCBjb25zdCBncmFiTWFuaWZlc3RKc29uRnJvbVJlcG9zaXRvcnkgPSBhc3luYyAocmVwb3NpdG9yeVBhdGg6IHN0cmluZywgcm9vdE1hbmlmZXN0ID0gdHJ1ZSwgZGVidWdMb2dnaW5nID0gdHJ1ZSk6IFByb21pc2U8UGx1Z2luTWFuaWZlc3R8bnVsbD4gPT4ge1xuICAgIGNvbnN0IG1hbmlmZXN0SnNvblBhdGggPSBHSVRIVUJfUkFXX1VTRVJDT05URU5UX1BBVEggKyByZXBvc2l0b3J5UGF0aCArXG4gICAgICAgIChyb290TWFuaWZlc3QgPT09IHRydWUgPyBcIi9IRUFEL21hbmlmZXN0Lmpzb25cIiA6IFwiL0hFQUQvbWFuaWZlc3QtYmV0YS5qc29uXCIpO1xuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IHJlc3BvbnNlID0gYXdhaXQgcmVxdWVzdCh7IHVybDogbWFuaWZlc3RKc29uUGF0aCB9KTtcbiAgICAgICAgcmV0dXJuIChyZXNwb25zZSA9PT0gXCI0MDQ6IE5vdCBGb3VuZFwiID8gbnVsbCA6IGF3YWl0IEpTT04ucGFyc2UocmVzcG9uc2UpKTtcbiAgICB9IGNhdGNoIChlcnJvcikge1xuICAgICAgICBpZihlcnJvciE9XCJFcnJvcjogUmVxdWVzdCBmYWlsZWQsIHN0YXR1cyA0MDRcIiAmJiBkZWJ1Z0xvZ2dpbmcpICB7IC8vbm9ybWFsIGVycm9yLCBpZ25vcmVcbiAgICAgICAgICAgIGNvbnNvbGUubG9nKGBlcnJvciBpbiBncmFiTWFuaWZlc3RKc29uRnJvbVJlcG9zaXRvcnkgZm9yICR7bWFuaWZlc3RKc29uUGF0aH1gLCBlcnJvcik7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxufVxuXG5cbmV4cG9ydCBjb25zdCBncmFiQ29tbW11bml0eVBsdWdpbkxpc3QgPSBhc3luYyAoZGVidWdMb2dnaW5nID0gdHJ1ZSk6IFByb21pc2U8SlNPTnxudWxsPiA9PiB7XG4gICAgY29uc3QgcGx1Z2luTGlzdFVSTCA9IGBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vb2JzaWRpYW5tZC9vYnNpZGlhbi1yZWxlYXNlcy9IRUFEL2NvbW11bml0eS1wbHVnaW5zLmpzb25gO1xuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IHJlc3BvbnNlID0gYXdhaXQgcmVxdWVzdCh7IHVybDogcGx1Z2luTGlzdFVSTCB9KTtcbiAgICAgICAgcmV0dXJuIChyZXNwb25zZSA9PT0gXCI0MDQ6IE5vdCBGb3VuZFwiID8gbnVsbCA6IGF3YWl0IEpTT04ucGFyc2UocmVzcG9uc2UpKTtcbiAgICB9IGNhdGNoIChlcnJvcikge1xuICAgICAgICBpZihkZWJ1Z0xvZ2dpbmcpIGNvbnNvbGUubG9nKFwiZXJyb3IgaW4gZ3JhYkNvbW1tdW5pdHlQbHVnaW5MaXN0XCIsIGVycm9yKVxuICAgICAgICByZXR1cm4gbnVsbDtcbiAgICB9XG59XG5cbmV4cG9ydCBjb25zdCBncmFiQ29tbW11bml0eVRoZW1lc0xpc3QgPSBhc3luYyAoZGVidWdMb2dnaW5nID0gdHJ1ZSk6IFByb21pc2U8SlNPTnxudWxsPiA9PiB7XG4gICAgY29uc3QgdGhlbWVzVVJMID0gYGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9vYnNpZGlhbm1kL29ic2lkaWFuLXJlbGVhc2VzL0hFQUQvY29tbXVuaXR5LWNzcy10aGVtZXMuanNvbmA7XG4gICAgdHJ5IHtcbiAgICAgICAgY29uc3QgcmVzcG9uc2UgPSBhd2FpdCByZXF1ZXN0KHsgdXJsOiB0aGVtZXNVUkwgfSk7XG4gICAgICAgIHJldHVybiAocmVzcG9uc2UgPT09IFwiNDA0OiBOb3QgRm91bmRcIiA/IG51bGwgOiBhd2FpdCBKU09OLnBhcnNlKHJlc3BvbnNlKSk7XG4gICAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICAgICAgaWYoZGVidWdMb2dnaW5nKSBjb25zb2xlLmxvZyhcImVycm9yIGluIGdyYWJDb21tbXVuaXR5VGhlbWVzTGlzdFwiLCBlcnJvcilcbiAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgfVxufVxuXG5cbmV4cG9ydCBjb25zdCBncmFiQ29tbW11bml0eVRoZW1lQ3NzRmlsZSA9IGFzeW5jIChyZXBvc2l0b3J5UGF0aDogc3RyaW5nLCBiZXRhVmVyc2lvbiA9IGZhbHNlLCBkZWJ1Z0xvZ2dpbmc6IGJvb2xlYW4pOiBQcm9taXNlPHN0cmluZ3xudWxsPiA9PiB7XG4gICAgY29uc3QgdGhlbWVzVVJMID0gYGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS8ke3JlcG9zaXRvcnlQYXRofS9IRUFEL3RoZW1lJHtiZXRhVmVyc2lvbiA/IFwiLWJldGFcIiA6IFwiXCJ9LmNzc2A7XG4gICAgdHJ5IHtcbiAgICAgICAgY29uc3QgcmVzcG9uc2UgPSBhd2FpdCByZXF1ZXN0KHsgdXJsOiB0aGVtZXNVUkwgfSk7XG4gICAgICAgIHJldHVybiAocmVzcG9uc2UgPT09IFwiNDA0OiBOb3QgRm91bmRcIiA/IG51bGwgOiByZXNwb25zZSk7XG4gICAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICAgICAgaWYoZGVidWdMb2dnaW5nKSBjb25zb2xlLmxvZyhcImVycm9yIGluIGdyYWJDb21tbXVuaXR5VGhlbWVDc3NGaWxlXCIsIGVycm9yKVxuICAgICAgICByZXR1cm4gbnVsbDtcbiAgICB9XG59XG5cbmV4cG9ydCBjb25zdCBncmFiQ29tbW11bml0eVRoZW1lTWFuaWZlc3RGaWxlID0gYXN5bmMgKHJlcG9zaXRvcnlQYXRoOiBzdHJpbmcsIGRlYnVnTG9nZ2luZyA9IHRydWUpOiBQcm9taXNlPHN0cmluZ3xudWxsPiA9PiB7XG4gICAgY29uc3QgdGhlbWVzVVJMID0gYGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS8ke3JlcG9zaXRvcnlQYXRofS9IRUFEL21hbmlmZXN0Lmpzb25gO1xuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IHJlc3BvbnNlID0gYXdhaXQgcmVxdWVzdCh7IHVybDogdGhlbWVzVVJMIH0pO1xuICAgICAgICByZXR1cm4gKHJlc3BvbnNlID09PSBcIjQwNDogTm90IEZvdW5kXCIgPyBudWxsIDogcmVzcG9uc2UpO1xuICAgIH0gY2F0Y2ggKGVycm9yKSB7XG4gICAgICAgIGlmKGRlYnVnTG9nZ2luZykgY29uc29sZS5sb2coXCJlcnJvciBpbiBncmFiQ29tbW11bml0eVRoZW1lTWFuaWZlc3RGaWxlXCIsIGVycm9yKVxuICAgICAgICByZXR1cm4gbnVsbDtcbiAgICB9XG59XG5cbmNvbnN0IGNoZWNrc3VtID0gKHN0cjogc3RyaW5nKTogbnVtYmVyID0+IHtcbiAgICBsZXQgc3VtID0gMDtcbiAgICBmb3IgKGxldCBpID0gMDsgaSA8IHN0ci5sZW5ndGg7IGkrKykge1xuICAgICAgICBzdW0gKz0gc3RyLmNoYXJDb2RlQXQoaSk7XG4gICAgfVxuICAgIHJldHVybiBzdW07XG59XG5cbmV4cG9ydCBjb25zdCBjaGVja3N1bUZvclN0cmluZyA9IChzdHI6IHN0cmluZyk6IHN0cmluZyA9PiB7XG4gICAgcmV0dXJuIGNoZWNrc3VtKHN0cikudG9TdHJpbmcoKTtcbn1cblxuZXhwb3J0IGNvbnN0IGdyYWJDaGVja3N1bU9mVGhlbWVDc3NGaWxlID0gYXN5bmMgKHJlcG9zaXRvcnlQYXRoOiBzdHJpbmcsIGJldGFWZXJzaW9uOiBib29sZWFuLCBkZWJ1Z0xvZ2dpbmc6IGJvb2xlYW4pOiBQcm9taXNlPHN0cmluZz4gPT57XG4gICAgY29uc3QgdGhlbWVDU1MgPSBhd2FpdCBncmFiQ29tbW11bml0eVRoZW1lQ3NzRmlsZShyZXBvc2l0b3J5UGF0aCwgYmV0YVZlcnNpb24sIGRlYnVnTG9nZ2luZylcbiAgICByZXR1cm4gdGhlbWVDU1MgPyBjaGVja3N1bUZvclN0cmluZyh0aGVtZUNTUykgOiBcIjBcIjtcbn1cblxuZXhwb3J0IGNvbnN0IGdyYWJMYXN0Q29tbWl0SW5mb0ZvckFGaWxlID0gYXN5bmMgKHJlcG9zaXRvcnlQYXRoOiBzdHJpbmcsIHBhdGg6IHN0cmluZywgZGVidWdMb2dnaW5nID0gdHJ1ZSk6IFByb21pc2U8c3RyaW5nfG51bGw+ID0+IHtcbiAgICBjb25zdCB1cmwgPSBgaHR0cHM6Ly9hcGkuZ2l0aHViLmNvbS9yZXBvcy8ke3JlcG9zaXRvcnlQYXRofS9jb21taXRzP3BhdGg9JHtwYXRofSZwYWdlPTEmcGVyX3BhZ2U9MWA7XG4gICAgdHJ5IHtcbiAgICAgICAgY29uc3QgcmVzcG9uc2UgPSBhd2FpdCByZXF1ZXN0KHsgdXJsOiB1cmwgfSk7XG4gICAgICAgIHJldHVybiAocmVzcG9uc2UgPT09IFwiNDA0OiBOb3QgRm91bmRcIiA/IG51bGwgOiBKU09OLnBhcnNlKHJlc3BvbnNlKSk7XG4gICAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICAgICAgaWYoZGVidWdMb2dnaW5nKSBjb25zb2xlLmxvZyhcImVycm9yIGluIGdyYWJMYXN0Q29tbWl0SW5mb0ZvckFGaWxlXCIsIGVycm9yKVxuICAgICAgICByZXR1cm4gbnVsbDtcbiAgICB9XG59XG5cbmV4cG9ydCBjb25zdCBncmFiTGFzdENvbW1pdERhdGVGb3JBRmlsZSA9IGFzeW5jIChyZXBvc2l0b3J5UGF0aDogc3RyaW5nLCBwYXRoOiBzdHJpbmcpOiBQcm9taXNlPHN0cmluZz4gPT4ge1xuICAgIGNvbnN0IHRlc3QgPSBhd2FpdCBncmFiTGFzdENvbW1pdEluZm9Gb3JBRmlsZShyZXBvc2l0b3J5UGF0aCwgcGF0aCk7XG4gICAgLy9AdHMtaWdub3JlXG4gICAgaWYodGVzdFswXS5jb21taXQuY29tbWl0dGVyLmRhdGUpe1xuICAgICAgICAvL0B0cy1pZ25vcmVcbiAgICAgICAgcmV0dXJuIHRlc3RbMF0uY29tbWl0LmNvbW1pdHRlci5kYXRlXG4gICAgfVxuICAgIGVsc2VcbiAgICAgICAgcmV0dXJuIFwiXCI7XG59XG5cbiIsICJpbXBvcnQgeyBjaGVja3N1bUZvclN0cmluZyB9IGZyb20gXCIuLi9mZWF0dXJlcy9naXRodWJVdGlsc1wiO1xuaW1wb3J0IFRoZVBsdWdpbiBmcm9tIFwiLi4vbWFpblwiO1xuXG5leHBvcnQgaW50ZXJmYWNlIFRoZW1lSW5mb3JhbXRpb24ge1xuICAgIHJlcG86IHN0cmluZztcbiAgICBsYXN0VXBkYXRlOiBzdHJpbmc7IC8vY2hlY2tzdW0gb2YgdGhlbWUgZmlsZSAoZWl0aGVyIHRoZW1lLmNzcyBvciB0aGVtZS1iZXRhLmNzcylcbn1cblxuZXhwb3J0IGludGVyZmFjZSBQbHVnaW5Gcm96ZW5WZXJzaW9uIHtcbiAgICByZXBvOiBzdHJpbmc7XG4gICAgdmVyc2lvbjogc3RyaW5nO1xufVxuXG5leHBvcnQgaW50ZXJmYWNlIFNldHRpbmdzIHtcbiAgICBwbHVnaW5MaXN0OiBzdHJpbmdbXTtcbiAgICBwbHVnaW5TdWJMaXN0RnJvemVuVmVyc2lvbjogUGx1Z2luRnJvemVuVmVyc2lvbltdLFxuICAgIHRoZW1lc0xpc3Q6IFRoZW1lSW5mb3JhbXRpb25bXTtcbiAgICB1cGRhdGVBdFN0YXJ0dXA6IGJvb2xlYW47XG4gICAgdXBkYXRlVGhlbWVzQXRTdGFydHVwOiAgYm9vbGVhbjtcbiAgICByaWJib25JY29uRW5hYmxlZDogYm9vbGVhbjtcbiAgICBsb2dnaW5nRW5hYmxlZDogYm9vbGVhbjtcbiAgICBsb2dnaW5nUGF0aDogc3RyaW5nO1xuICAgIGxvZ2dpbmdWZXJib3NlRW5hYmxlZDogYm9vbGVhbjtcbiAgICBkZWJ1Z2dpbmdNb2RlOiBib29sZWFuO1xuICAgIG5vdGlmaWNhdGlvbnNFbmFibGVkOiBib29sZWFuO1xufVxuXG5leHBvcnQgY29uc3QgREVGQVVMVF9TRVRUSU5HUzogU2V0dGluZ3MgPSB7XG4gICAgcGx1Z2luTGlzdDogW10sXG4gICAgcGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb246IFtdLFxuICAgIHRoZW1lc0xpc3Q6IFtdLFxuICAgIHVwZGF0ZUF0U3RhcnR1cDogZmFsc2UsXG4gICAgdXBkYXRlVGhlbWVzQXRTdGFydHVwOiBmYWxzZSxcbiAgICByaWJib25JY29uRW5hYmxlZDogdHJ1ZSxcbiAgICBsb2dnaW5nRW5hYmxlZDogZmFsc2UsXG4gICAgbG9nZ2luZ1BhdGg6IFwiQlJBVC1sb2dcIixcbiAgICBsb2dnaW5nVmVyYm9zZUVuYWJsZWQ6IGZhbHNlLFxuICAgIGRlYnVnZ2luZ01vZGU6IHRydWUsXG4gICAgbm90aWZpY2F0aW9uc0VuYWJsZWQ6IHRydWVcbn1cblxuLyoqXG4gKiBBZGRzIGEgcGx1Z2luIGZvciBiZXRhIHRlc3RpbmcgdG8gdGhlIGRhdGEuanNvbiBmaWxlIG9mIHRoaXMgIHBsdWdpblxuICpcbiAqIEBwYXJhbSAgIHtUaGVQbHVnaW59ICAgICAgcGx1Z2luICAgICAgICAgXG4gKiBAcGFyYW0gICB7c3RyaW5nPHZvaWQ+fSAgIHJlcG9zaXRvcnlQYXRoICBwYXRoIHRvIHRoZSBHaXRIdWIgcmVwb3NpdG9yeVxuICogQHBhcmFtICAge3N0cmluZ30gICAgICAgICBzcGVjaWZ5VmVyc2lvbiAgaWYgdGhlIHBsdWdpbiBuZWVkcyB0byBzdGF5IGF0IHRoZSBmcm96ZW4gdmVyc2lvbiwgd2UgbmVlZCB0byBhbHNvIHJlY29yZCB0aGUgdmVyc2lvblxuICpcbiAqIEByZXR1cm4gIHtQcm9taXNlPHZvaWQ+fSAgICAgICAgICAgICAgICAgIFxuICovXG5leHBvcnQgYXN5bmMgZnVuY3Rpb24gYWRkQmV0YVBsdWdpblRvTGlzdChwbHVnaW46IFRoZVBsdWdpbiwgcmVwb3NpdG9yeVBhdGg6IHN0cmluZywgc3BlY2lmeVZlcnNpb24gPSBcIlwiKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgbGV0IHNhdmUgPSBmYWxzZTtcbiAgICBpZiAoIXBsdWdpbi5zZXR0aW5ncy5wbHVnaW5MaXN0LmNvbnRhaW5zKHJlcG9zaXRvcnlQYXRoKSkge1xuICAgICAgICBwbHVnaW4uc2V0dGluZ3MucGx1Z2luTGlzdC51bnNoaWZ0KHJlcG9zaXRvcnlQYXRoKTtcbiAgICAgICAgc2F2ZSA9IHRydWU7XG4gICAgfVxuICAgIGlmIChcbiAgICAgICAgc3BlY2lmeVZlcnNpb24gIT09IFwiXCIgXG4gICAgICAgICYmIChwbHVnaW4uc2V0dGluZ3MucGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb24uZmlsdGVyKHggPT4geC5yZXBvID09PSByZXBvc2l0b3J5UGF0aCkubGVuZ3RoID09PSAwKVxuICAgICkge1xuICAgICAgICBwbHVnaW4uc2V0dGluZ3MucGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb24udW5zaGlmdCh7XG4gICAgICAgICAgICByZXBvOiByZXBvc2l0b3J5UGF0aCxcbiAgICAgICAgICAgIHZlcnNpb246IHNwZWNpZnlWZXJzaW9uXG4gICAgICAgIH0pO1xuICAgICAgICBzYXZlID0gdHJ1ZTtcbiAgICB9XG4gICAgaWYgKHNhdmUpIHtcbiAgICAgICAgcGx1Z2luLnNhdmVTZXR0aW5ncygpO1xuICAgIH1cbn1cblxuLyoqXG4gKiBUZXN0cyBpZiAgYSAgcGx1Z2luICBpcyBpbiBkYXRhLmpzb25cbiAqXG4gKiBAcGFyYW0gICB7VGhlUGx1Z2lufSAgICAgICAgIHBsdWdpbiAgICAgICAgICBcbiAqIEBwYXJhbSAgIHtzdHJpbmc8Ym9vbGVhbj59ICAgcmVwb3NpdG9yeVBhdGggIHBhdGggdG8gdGhlIEdpdEh1YiByZXBvc2l0b3J5XG4gKlxuICogQHJldHVybiAge1Byb21pc2U8Ym9vbGVhbj59ICB0cnVlIGlmIGV4aXN0cyAgICAgIFxuICovXG5leHBvcnQgYXN5bmMgZnVuY3Rpb24gZXhpc3RCZXRhUGx1Z2luSW5MaXN0KHBsdWdpbjogVGhlUGx1Z2luLCByZXBvc2l0b3J5UGF0aDogc3RyaW5nKTogUHJvbWlzZTxib29sZWFuPiB7XG4gICAgcmV0dXJuIHBsdWdpbi5zZXR0aW5ncy5wbHVnaW5MaXN0LmNvbnRhaW5zKHJlcG9zaXRvcnlQYXRoKTtcbn1cblxuXG4vKipcbiAqIEFkZHMgYSB0aGVtZSBmb3IgYmV0YSB0ZXN0aW5nIHRvIHRoZSBkYXRhLmpzb24gZmlsZSBvZiB0aGlzICBwbHVnaW5cbiAqXG4gKiBAcGFyYW0gICB7VGhlUGx1Z2lufSAgICAgIHBsdWdpbiAgICAgICAgIFxuICogQHBhcmFtICAge3N0cmluZzx2b2lkPn0gICByZXBvc2l0b3J5UGF0aCAgcGF0aCB0byB0aGUgR2l0SHViIHJlcG9zaXRvcnlcbiAqIEBwYXJhbSAgIHtzdHJpbmc8dm9pZD59ICAgdGhlbWVDU1MgIHJhdyB0ZXh0IG9mIHRoZSB0aGVtZS4gSXQgaXMgY2hlY2tzdW1tZWQgYW5kIHRoaXMgaXMgdXNlZCBmb3IgdHJhY2tpbmcgaWYgY2hhbmdlcyBvY2N1cnJlZCB0byB0aGUgdGhlbWVcbiAqXG4gKiBAcmV0dXJuICB7UHJvbWlzZTx2b2lkPn0gICAgICAgICAgICAgICAgICBcbiAqL1xuIGV4cG9ydCBhc3luYyBmdW5jdGlvbiBhZGRCZXRhVGhlbWVUb0xpc3QocGx1Z2luOiBUaGVQbHVnaW4sIHJlcG9zaXRvcnlQYXRoOiBzdHJpbmcsIHRoZW1lQ1NTOiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgY29uc3QgbmV3VGhlbWU6IFRoZW1lSW5mb3JhbXRpb24gPSB7IFxuICAgICAgICAgcmVwbzogcmVwb3NpdG9yeVBhdGgsIFxuICAgICAgICAgbGFzdFVwZGF0ZTogY2hlY2tzdW1Gb3JTdHJpbmcodGhlbWVDU1MpXG4gICAgfVxuICAgIHBsdWdpbi5zZXR0aW5ncy50aGVtZXNMaXN0LnVuc2hpZnQobmV3VGhlbWUpO1xuICAgIHBsdWdpbi5zYXZlU2V0dGluZ3MoKTtcbn1cblxuLyoqXG4gKiBUZXN0cyBpZiBhICB0aGVtZSAgaXMgaW4gZGF0YS5qc29uXG4gKlxuICogQHBhcmFtICAge1RoZVBsdWdpbn0gICAgICAgICBwbHVnaW4gICAgICAgICAgXG4gKiBAcGFyYW0gICB7c3RyaW5nPGJvb2xlYW4+fSAgIHJlcG9zaXRvcnlQYXRoICBwYXRoIHRvIHRoZSBHaXRIdWIgcmVwb3NpdG9yeVxuICpcbiAqIEByZXR1cm4gIHtQcm9taXNlPGJvb2xlYW4+fSAgdHJ1ZSBpZiBleGlzdHMgICAgICBcbiAqL1xuZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIGV4aXN0QmV0YVRoZW1laW5Jbkxpc3QocGx1Z2luOiBUaGVQbHVnaW4sIHJlcG9zaXRvcnlQYXRoOiBzdHJpbmcpOiBQcm9taXNlPGJvb2xlYW4+IHtcbiAgICBjb25zdCB0ZXN0SWZUaGVtRXhpc3RzID0gcGx1Z2luLnNldHRpbmdzLnRoZW1lc0xpc3QuZmluZCh0PT4gdC5yZXBvID09PSByZXBvc2l0b3J5UGF0aCk7XG4gICAgcmV0dXJuIHRlc3RJZlRoZW1FeGlzdHMgPyB0cnVlIDogZmFsc2U7XG59XG5cblxuLyoqXG4gKiBVcGRhdGUgdGhlIGxhc3RVcGF0ZSBmaWVsZCBmb3IgdGhlIHRoZW1lXG4gKlxuICogQHBhcmFtICAge1RoZVBsdWdpbn0gICAgICAgICBwbHVnaW4gICAgICAgICAgXG4gKiBAcGFyYW0gICB7c3RyaW5nPGJvb2xlYW4+fSAgIHJlcG9zaXRvcnlQYXRoICBwYXRoIHRvIHRoZSBHaXRIdWIgcmVwb3NpdG9yeVxuICogQHBhcmFtICAge3N0cmluZzxjaGVja3N1bT59ICBjaGVja3N1bSAgY2hlY2tzdW0gb2YgZmlsZS4gSW4gcGFzdCB3ZSB1c2VkIHRoZSBkYXRlIG9mIGZpbGUgdXBkYXRlLCBidXQgdGhpcyBwcm92ZWQgdG8gbm90IGJlIGNvbnNpc2VudCB3aXRoIHRoZSBHaXRIdWIgY2FjaGUuXG4gKlxuICovXG4gZXhwb3J0IGZ1bmN0aW9uIHVwZGF0ZUJldGFUaGVtZUxhc3RVcGRhdGVDaGVja3N1bShwbHVnaW46IFRoZVBsdWdpbiwgcmVwb3NpdG9yeVBhdGg6IHN0cmluZywgY2hlY2tzdW06IHN0cmluZyk6IHZvaWQge1xuICAgIHBsdWdpbi5zZXR0aW5ncy50aGVtZXNMaXN0LmZvckVhY2godD0+e1xuICAgICAgICBpZih0LnJlcG8gPT09IHJlcG9zaXRvcnlQYXRoKSB7XG4gICAgICAgICAgICB0Lmxhc3RVcGRhdGUgPSBjaGVja3N1bTtcbiAgICAgICAgICAgIHBsdWdpbi5zYXZlU2V0dGluZ3MoKTtcbiAgICAgICAgfVxuICAgIH0pO1xufVxuXG4iLCAiaW1wb3J0IHsgTm90aWNlLCBQbGF0Zm9ybSB9IGZyb20gXCJvYnNpZGlhblwiO1xuaW1wb3J0IFRoZVBsdWdpbiBmcm9tIFwiLi4vbWFpblwiO1xuXG4vKipcbiAqIERpc3BsYXlzIGEgbm90aWNlIHRvIHRoZSB1c2VyXG4gKlxuICogQHBhcmFtICAge1RoZVBsdWdpbn0gIHBsdWdpbiAgICAgICAgICAgICAgUGx1Z2luIG9iamVjdFxuICogQHBhcmFtICAge3N0cmluZ30gICAgIG1zZyAgICAgICAgICAgICAgICAgVGV4dCB0byBkaXNwbGF5IHRvIHRoZSB1c2VyXG4gKiBAcGFyYW0gICB7bnVtYmVyfSAgICAgdGltZW91dEluU2Vjb25kcyAgICBOdW1iZXIgb2Ygc2Vjb25kcyB0byBzaG93IHRoZSBUb2FzdCBtZXNzYWdlXG4gKiBAcGFyYW0gICB7bnVsbH0gICAgICAgY29udGV4dE1lbnVDYWxsYmFjayBmdW5jdGlvbiB0byBjYWxsIGlmIHJpZ2h0IG1vdXNlIGNsaWNrZWRcbiAqIEByZXR1cm4gIHt2b2lkfSAgICAgICAgICAgICAgICAgICAgICAgICBcbiAqL1xuZXhwb3J0IGZ1bmN0aW9uIFRvYXN0TWVzc2FnZShwbHVnaW46IFRoZVBsdWdpbiwgbXNnOiBzdHJpbmcsIHRpbWVvdXRJblNlY29uZHMgPSAxMCwgY29udGV4dE1lbnVDYWxsYmFjaz86KCk9PnZvaWQpOiB2b2lkIHtcbiAgICBpZihwbHVnaW4uc2V0dGluZ3Mubm90aWZpY2F0aW9uc0VuYWJsZWQ9PT1mYWxzZSkgcmV0dXJuO1xuICAgIGNvbnN0IGFkZGl0aW9uYWxJbmZvID0gY29udGV4dE1lbnVDYWxsYmFjayAgPyBcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAoUGxhdGZvcm0uaXNEZXNrdG9wID8gXCIoY2xpY2s9ZGlzbWlzcywgcmlnaHQtY2xpY2s9SW5mbylcIiA6IFwiKGNsaWNrPWRpc21pc3MpXCIpIDogXCJcIjtcbiAgICBjb25zdCBuZXdOb3RpY2U6IE5vdGljZSA9IG5ldyBOb3RpY2UoYEJSQVRcXG4ke21zZ31cXG4ke2FkZGl0aW9uYWxJbmZvfWAsIHRpbWVvdXRJblNlY29uZHMqMTAwMCk7XG4gICAgLy9AdHMtaWdub3JlXG4gICAgaWYoY29udGV4dE1lbnVDYWxsYmFjaykgbmV3Tm90aWNlLm5vdGljZUVsLm9uY29udGV4dG1lbnUgPSBhc3luYyAoKSA9PiB7IGNvbnRleHRNZW51Q2FsbGJhY2soKSB9OyAgICBcbn0iLCAiXG4vKipcbiAqIFRlc3RzIGlmIHRoZXJlIGlzIGFuIGludGVybmV0IGNvbm5lY3Rpb25cbiAqIEByZXR1cm5zIHRydWUgaWYgY29ubmVjdGVkLCBmYWxzZSBpZiBubyBpbnRlcm5ldFxuICovXG5leHBvcnQgYXN5bmMgZnVuY3Rpb24gaXNDb25uZWN0ZWRUb0ludGVybmV0KCk6IFByb21pc2U8Ym9vbGVhbj4ge1xuICAgIHRyeSB7XG4gICAgICAgIGNvbnN0IG9ubGluZSA9IGF3YWl0IGZldGNoKFwiaHR0cHM6Ly9vYnNpZGlhbi5tZC8/XCIgKyBNYXRoLnJhbmRvbSgpKTtcbiAgICAgICAgcmV0dXJuIG9ubGluZS5zdGF0dXMgPj0gMjAwICYmIG9ubGluZS5zdGF0dXMgPCAzMDA7XG4gICAgfSBjYXRjaChlcnIpIHtcbiAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgIH1cbn0iLCAiaW1wb3J0IHsgTW9kYWwsIFNldHRpbmcgfSBmcm9tICdvYnNpZGlhbic7XG5pbXBvcnQgeyB0aGVtZVNhdmUgfSBmcm9tICcuLi9mZWF0dXJlcy90aGVtZXMnO1xuaW1wb3J0IFRoZVBsdWdpbiBmcm9tICcuLi9tYWluJztcbmltcG9ydCB7IFRvYXN0TWVzc2FnZSB9IGZyb20gJy4uL3V0aWxzL25vdGlmaWNhdGlvbnMnO1xuaW1wb3J0IHsgIGV4aXN0QmV0YVRoZW1laW5Jbkxpc3QgfSBmcm9tICcuL3NldHRpbmdzJztcbmltcG9ydCB7IHByb21vdGlvbmFsTGlua3MgfSBmcm9tICcuL1Byb21vdGlvbmFsJztcblxuLyoqXG4gKiBBZGQgYSBiZXRhIHRoZW1lIHRvIHRoZSBsaXN0IG9mIHBsdWdpbnMgYmVpbmcgdHJhY2tlZCBhbmQgdXBkYXRlZFxuICovXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBBZGROZXdUaGVtZSBleHRlbmRzIE1vZGFsIHtcbiAgICBwbHVnaW46IFRoZVBsdWdpbjtcbiAgICBhZGRyZXNzOiBzdHJpbmc7XG4gICAgb3BlblNldHRpbmdzVGFiQWZ0ZXJ3YXJkczogYm9vbGVhbjtcblxuICAgIGNvbnN0cnVjdG9yKHBsdWdpbjogVGhlUGx1Z2luLCBvcGVuU2V0dGluZ3NUYWJBZnRlcndhcmRzID0gZmFsc2UpIHtcbiAgICAgICAgc3VwZXIocGx1Z2luLmFwcCk7XG4gICAgICAgIHRoaXMucGx1Z2luID0gcGx1Z2luO1xuICAgICAgICB0aGlzLmFkZHJlc3MgPSBcIlwiO1xuICAgICAgICB0aGlzLm9wZW5TZXR0aW5nc1RhYkFmdGVyd2FyZHMgPSBvcGVuU2V0dGluZ3NUYWJBZnRlcndhcmRzO1xuICAgIH1cblxuICAgIGFzeW5jIHN1Ym1pdEZvcm0oKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICAgIGlmICh0aGlzLmFkZHJlc3MgPT09IFwiXCIpIHJldHVybjtcbiAgICAgICAgY29uc3Qgc2NydWJiZWRBZGRyZXNzID0gdGhpcy5hZGRyZXNzLnJlcGxhY2UoXCJodHRwczovL2dpdGh1Yi5jb20vXCIsIFwiXCIpO1xuICAgICAgICBpZiAoYXdhaXQgZXhpc3RCZXRhVGhlbWVpbkluTGlzdCh0aGlzLnBsdWdpbiwgc2NydWJiZWRBZGRyZXNzKSkge1xuICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBgVGhpcyBwbHVnaW4gaXMgYWxyZWFkeSBpbiB0aGUgbGlzdCBmb3IgYmV0YSB0ZXN0aW5nYCwgMTApO1xuICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIFxuICAgICAgICBpZihhd2FpdCB0aGVtZVNhdmUodGhpcy5wbHVnaW4sIHNjcnViYmVkQWRkcmVzcywgdHJ1ZSkpIHtcbiAgICAgICAgICAgIHRoaXMuY2xvc2UoKTsgICAgXG4gICAgICAgIH1cbiAgICB9XG5cbiAgICBvbk9wZW4oKTogdm9pZCB7XG4gICAgICAgIHRoaXMuY29udGVudEVsLmNyZWF0ZUVsKCdoNCcsIHsgdGV4dDogXCJHaXRodWIgcmVwb3NpdG9yeSBmb3IgYmV0YSB0aGVtZTpcIiB9KTtcbiAgICAgICAgdGhpcy5jb250ZW50RWwuY3JlYXRlRWwoJ2Zvcm0nLCB7fSwgKGZvcm1FbCkgPT4ge1xuICAgICAgICAgICAgZm9ybUVsLmFkZENsYXNzKFwiYnJhdC1tb2RhbFwiKTtcbiAgICAgICAgICAgIG5ldyBTZXR0aW5nKGZvcm1FbClcbiAgICAgICAgICAgICAgICAuYWRkVGV4dCgodGV4dEVsKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHRleHRFbC5zZXRQbGFjZWhvbGRlcignUmVwb3NpdG9yeSAoZXhhbXBsZTogaHR0cHM6Ly9naXRodWIuY29tL0dpdHViVXNlck5hbWUvcmVwb3NpdG9yeS1uYW1lJyk7XG4gICAgICAgICAgICAgICAgICAgIHRleHRFbC5vbkNoYW5nZSgodmFsdWUpID0+IHtcbiAgICAgICAgICAgICAgICAgICAgICAgIHRoaXMuYWRkcmVzcyA9IHZhbHVlLnRyaW0oKTtcbiAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICAgICAgICAgIHRleHRFbC5pbnB1dEVsLmFkZEV2ZW50TGlzdGVuZXIoJ2tleWRvd24nLCBhc3luYyAoZTogS2V5Ym9hcmRFdmVudCkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKGUua2V5ID09PSAnRW50ZXInICYmIHRoaXMuYWRkcmVzcyAhPT0gJyAnKSB7XG4gICAgICAgICAgICAgICAgICAgICAgICAgICAgZS5wcmV2ZW50RGVmYXVsdCgpO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGF3YWl0IHRoaXMuc3VibWl0Rm9ybSgpO1xuICAgICAgICAgICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgICAgICAgICAgdGV4dEVsLmlucHV0RWwuc3R5bGUud2lkdGggPSBcIjEwMCVcIjtcbiAgICAgICAgICAgICAgICAgICAgd2luZG93LnNldFRpbWVvdXQoKCkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgY29uc3QgdGl0bGUgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKFwiLnNldHRpbmctaXRlbS1pbmZvXCIpO1xuICAgICAgICAgICAgICAgICAgICAgICAgaWYgKHRpdGxlKSB0aXRsZS5yZW1vdmUoKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIHRleHRFbC5pbnB1dEVsLmZvY3VzKClcbiAgICAgICAgICAgICAgICAgICAgfSwgMTApO1xuICAgICAgICAgICAgICAgIH0pO1xuXG4gICAgICAgICAgICBmb3JtRWwuY3JlYXRlRGl2KCdtb2RhbC1idXR0b24tY29udGFpbmVyJywgKGJ1dHRvbkNvbnRhaW5lckVsKSA9PiB7XG4gICAgICAgICAgICAgICAgYnV0dG9uQ29udGFpbmVyRWxcbiAgICAgICAgICAgICAgICAgICAgLmNyZWF0ZUVsKCdidXR0b24nLCB7IGF0dHI6IHsgdHlwZTogJ2J1dHRvbicgfSwgdGV4dDogJ05ldmVyIG1pbmQnIH0pXG4gICAgICAgICAgICAgICAgICAgIC5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsICgpID0+IHRoaXMuY2xvc2UoKSk7XG4gICAgICAgICAgICAgICAgYnV0dG9uQ29udGFpbmVyRWwuY3JlYXRlRWwoJ2J1dHRvbicsIHtcbiAgICAgICAgICAgICAgICAgICAgYXR0cjogeyB0eXBlOiAnc3VibWl0JyB9LFxuICAgICAgICAgICAgICAgICAgICBjbHM6ICdtb2QtY3RhJyxcbiAgICAgICAgICAgICAgICAgICAgdGV4dDogJ0FkZCBUaGVtZScsXG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9KTtcblxuICAgICAgICAgICAgY29uc3QgbmV3RGl2ID0gZm9ybUVsLmNyZWF0ZURpdigpO1xuICAgICAgICAgICAgbmV3RGl2LnN0eWxlLmJvcmRlclRvcCA9IFwiMXB4IHNvbGlkICNjY2NcIjtcbiAgICAgICAgICAgIG5ld0Rpdi5zdHlsZS5tYXJnaW5Ub3AgPSBcIjMwcHhcIjtcbiAgICAgICAgICAgIGNvbnN0IGJ5VGZUaGFja2VyID0gbmV3RGl2LmNyZWF0ZVNwYW4oKTtcbiAgICAgICAgICAgIGJ5VGZUaGFja2VyLmlubmVySFRNTCA9IFwiQlJBVCBieSA8YSBocmVmPSdodHRwczovL2JpdC5seS9vNDItdHdpdHRlcic+VEZUSGFja2VyPC9hPlwiO1xuICAgICAgICAgICAgYnlUZlRoYWNrZXIuc3R5bGUuZm9udFN0eWxlID0gXCJpdGFsaWNcIjtcbiAgICAgICAgICAgIG5ld0Rpdi5hcHBlbmRDaGlsZChieVRmVGhhY2tlcik7XG4gICAgICAgICAgICBwcm9tb3Rpb25hbExpbmtzKG5ld0RpdiwgZmFsc2UpO1xuXG4gICAgICAgICAgICB3aW5kb3cuc2V0VGltZW91dCgoKSA9PiB7XG4gICAgICAgICAgICAgICAgY29uc3QgdGl0bGUgPSBmb3JtRWwucXVlcnlTZWxlY3RvckFsbChcIi5icmF0LW1vZGFsIC5zZXR0aW5nLWl0ZW0taW5mb1wiKTtcbiAgICAgICAgICAgICAgICB0aXRsZS5mb3JFYWNoKCh0aXRsZUVsKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHRpdGxlRWwucmVtb3ZlKCk7XG4gICAgICAgICAgICAgICAgfSlcbiAgICAgICAgICAgIH0sIDUwKVxuXG4gICAgICAgICAgICAvLyBpbnZva2VkIHdoZW4gYnV0dG9uIGlzIGNsaWNrZWQuIFxuICAgICAgICAgICAgZm9ybUVsLmFkZEV2ZW50TGlzdGVuZXIoJ3N1Ym1pdCcsIGFzeW5jIChlOiBFdmVudCkgPT4ge1xuICAgICAgICAgICAgICAgIGUucHJldmVudERlZmF1bHQoKTtcbiAgICAgICAgICAgICAgICBpZiAodGhpcy5hZGRyZXNzICE9PSAnJykgYXdhaXQgdGhpcy5zdWJtaXRGb3JtKCk7XG4gICAgICAgICAgICB9KTtcbiAgICAgICAgfSk7XG4gICAgfVxuXG4gICAgYXN5bmMgb25DbG9zZSgpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgICAgaWYgKHRoaXMub3BlblNldHRpbmdzVGFiQWZ0ZXJ3YXJkcykge1xuICAgICAgICAgICAgYXdhaXQgKHRoaXMucGx1Z2luIGFzIGFueSkuYXBwLnNldHRpbmcub3BlbigpO1xuICAgICAgICAgICAgYXdhaXQgKHRoaXMucGx1Z2luIGFzIGFueSkuYXBwLnNldHRpbmcub3BlblRhYkJ5SWQoXCJvYnNpZGlhbjQyLWJyYXRcIik7XG4gICAgICAgIH1cblxuICAgIH1cbn0iLCAiXG5cbmV4cG9ydCBjb25zdCBwcm9tb3Rpb25hbExpbmtzID0gKGNvbnRhaW5lckVsOiBIVE1MRWxlbWVudCwgc2V0dGluZ3NUYWIgPSB0cnVlKSA6IEhUTUxFbGVtZW50ID0+IHtcblxuICAgIGNvbnN0IGxpbmtzRGl2ID0gY29udGFpbmVyRWwuY3JlYXRlRWwoXCJkaXZcIik7XG4gICAgbGlua3NEaXYuc3R5bGUuZmxvYXQgPSBcInJpZ2h0XCI7XG4gICAgXG4gICAgaWYoc2V0dGluZ3NUYWI9PT1mYWxzZSkge1xuICAgICAgICBsaW5rc0Rpdi5zdHlsZS5wYWRkaW5nID0gXCIxMHB4XCI7XG4gICAgICAgIGxpbmtzRGl2LnN0eWxlLnBhZGRpbmdMZWZ0ID0gXCIxNXB4XCI7XG4gICAgICAgIGxpbmtzRGl2LnN0eWxlLnBhZGRpbmdSaWdodCA9IFwiMTVweFwiO1xuICAgIH0gZWxzZSB7XG4gICAgICAgIGxpbmtzRGl2LnN0eWxlLnBhZGRpbmcgPSBcIjE1cHhcIjtcbiAgICAgICAgbGlua3NEaXYuc3R5bGUucGFkZGluZ0xlZnQgPSBcIjE1cHhcIjtcbiAgICAgICAgbGlua3NEaXYuc3R5bGUucGFkZGluZ1JpZ2h0ID0gXCIxNXB4XCI7XG4gICAgICAgIGxpbmtzRGl2LnN0eWxlLm1hcmdpbkxlZnQgPSBcIjE1cHhcIjsgICAgXG4gICAgfVxuICAgIFxuICAgIGNvbnN0IHR3aXR0ZXJTcGFuID0gbGlua3NEaXYuY3JlYXRlRGl2KFwiY29mZmVlXCIpO1xuICAgIHR3aXR0ZXJTcGFuLmFkZENsYXNzKFwiZXgtdHdpdHRlci1zcGFuXCIpO1xuICAgIHR3aXR0ZXJTcGFuLnN0eWxlLnBhZGRpbmdMZWZ0ID0gXCIxMHB4XCI7XG4gICAgY29uc3QgY2FwdGlvblRleHQgPSB0d2l0dGVyU3Bhbi5jcmVhdGVEaXYoKTtcbiAgICBjYXB0aW9uVGV4dC5pbm5lclRleHQgPSBcIkxlYXJuIG1vcmUgYWJvdXQgbXkgd29yayBhdDpcIjtcbiAgICB0d2l0dGVyU3Bhbi5hcHBlbmRDaGlsZChjYXB0aW9uVGV4dClcbiAgICBjb25zdCB0d2l0dGVyTGluayA9IHR3aXR0ZXJTcGFuLmNyZWF0ZUVsKFwiYVwiLCB7IGhyZWY6IFwiaHR0cHM6Ly90ZnRoYWNrZXIuY29tXCIgfSk7XG4gICAgdHdpdHRlckxpbmsuaW5uZXJUZXh0ID0gXCJodHRwczovL3RmdGhhY2tlci5jb21cIjtcblxuXG4gICAgcmV0dXJuIGxpbmtzRGl2O1xufVxuXG4iLCAiaW1wb3J0IHsgTW9kYWwsIFNldHRpbmcgfSBmcm9tICdvYnNpZGlhbic7XG5pbXBvcnQgQmV0YVBsdWdpbnMgZnJvbSAnLi4vZmVhdHVyZXMvQmV0YVBsdWdpbnMnO1xuaW1wb3J0IFRoZVBsdWdpbiBmcm9tICcuLi9tYWluJztcbmltcG9ydCB7IFRvYXN0TWVzc2FnZSB9IGZyb20gJy4uL3V0aWxzL25vdGlmaWNhdGlvbnMnO1xuaW1wb3J0IHsgcHJvbW90aW9uYWxMaW5rcyB9IGZyb20gJy4vUHJvbW90aW9uYWwnO1xuaW1wb3J0IHsgZXhpc3RCZXRhUGx1Z2luSW5MaXN0IH0gZnJvbSAnLi9zZXR0aW5ncyc7XG5cbi8qKlxuICogQWRkIGEgYmV0YSBwbHVnaW4gdG8gdGhlIGxpc3Qgb2YgcGx1Z2lucyBiZWluZyB0cmFja2VkIGFuZCB1cGRhdGVkXG4gKi9cbmV4cG9ydCBkZWZhdWx0IGNsYXNzIEFkZE5ld1BsdWdpbk1vZGFsIGV4dGVuZHMgTW9kYWwge1xuICAgIHBsdWdpbjogVGhlUGx1Z2luO1xuICAgIGJldGFQbHVnaW5zOiBCZXRhUGx1Z2lucztcbiAgICBhZGRyZXNzOiBzdHJpbmc7XG4gICAgb3BlblNldHRpbmdzVGFiQWZ0ZXJ3YXJkczogYm9vbGVhbjtcbiAgICByZWFkb25seSB1c2VGcm96ZW5WZXJzaW9uOiBib29sZWFuO1xuICAgIHZlcnNpb246IHN0cmluZztcblxuICAgIGNvbnN0cnVjdG9yKHBsdWdpbjogVGhlUGx1Z2luLCBiZXRhUGx1Z2luczogQmV0YVBsdWdpbnMsIG9wZW5TZXR0aW5nc1RhYkFmdGVyd2FyZHMgPSBmYWxzZSwgdXNlRnJvemVuVmVyc2lvbiA9IGZhbHNlKSB7XG4gICAgICAgIHN1cGVyKHBsdWdpbi5hcHApO1xuICAgICAgICB0aGlzLnBsdWdpbiA9IHBsdWdpbjtcbiAgICAgICAgdGhpcy5iZXRhUGx1Z2lucyA9IGJldGFQbHVnaW5zO1xuICAgICAgICB0aGlzLmFkZHJlc3MgPSBcIlwiO1xuICAgICAgICB0aGlzLm9wZW5TZXR0aW5nc1RhYkFmdGVyd2FyZHMgPSBvcGVuU2V0dGluZ3NUYWJBZnRlcndhcmRzO1xuICAgICAgICB0aGlzLnVzZUZyb3plblZlcnNpb24gPSB1c2VGcm96ZW5WZXJzaW9uO1xuICAgICAgICB0aGlzLnZlcnNpb24gPSBcIlwiO1xuICAgIH1cblxuICAgIGFzeW5jIHN1Ym1pdEZvcm0oKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICAgIGlmICh0aGlzLmFkZHJlc3MgPT09IFwiXCIpIHJldHVybjtcbiAgICAgICAgbGV0IHNjcnViYmVkQWRkcmVzcyA9IHRoaXMuYWRkcmVzcy5yZXBsYWNlKFwiaHR0cHM6Ly9naXRodWIuY29tL1wiLFwiXCIpO1xuICAgICAgICBpZiAoc2NydWJiZWRBZGRyZXNzLmVuZHNXaXRoKFwiLmdpdFwiKSkgXG4gICAgICAgICAgICBzY3J1YmJlZEFkZHJlc3MgPSBzY3J1YmJlZEFkZHJlc3Muc2xpY2UoMCwgLTQpO1xuICAgICAgICBpZiAoYXdhaXQgZXhpc3RCZXRhUGx1Z2luSW5MaXN0KHRoaXMucGx1Z2luLCBzY3J1YmJlZEFkZHJlc3MpKSB7XG4gICAgICAgICAgICBUb2FzdE1lc3NhZ2UodGhpcy5wbHVnaW4sIGBUaGlzIHBsdWdpbiBpcyBhbHJlYWR5IGluIHRoZSBsaXN0IGZvciBiZXRhIHRlc3RpbmdgLCAxMCk7XG4gICAgICAgICAgICByZXR1cm47XG4gICAgICAgIH1cbiAgICAgICAgY29uc3QgcmVzdWx0ID0gYXdhaXQgdGhpcy5iZXRhUGx1Z2lucy5hZGRQbHVnaW4oc2NydWJiZWRBZGRyZXNzLCBmYWxzZSwgZmFsc2UsIGZhbHNlLCB0aGlzLnZlcnNpb24pO1xuICAgICAgICBpZiAocmVzdWx0KSB7XG4gICAgICAgICAgICB0aGlzLmNsb3NlKCk7XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICBvbk9wZW4oKTogdm9pZCB7XG4gICAgICAgIHRoaXMuY29udGVudEVsLmNyZWF0ZUVsKCdoNCcsIHsgdGV4dDogXCJHaXRodWIgcmVwb3NpdG9yeSBmb3IgYmV0YSBwbHVnaW46XCIgfSk7XG4gICAgICAgIHRoaXMuY29udGVudEVsLmNyZWF0ZUVsKCdmb3JtJywge30sIChmb3JtRWwpID0+IHtcbiAgICAgICAgICAgIGZvcm1FbC5hZGRDbGFzcyhcImJyYXQtbW9kYWxcIilcbiAgICAgICAgICAgIG5ldyBTZXR0aW5nKGZvcm1FbClcbiAgICAgICAgICAgICAgICAuYWRkVGV4dCgodGV4dEVsKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHRleHRFbC5zZXRQbGFjZWhvbGRlcignUmVwb3NpdG9yeSAoZXhhbXBsZTogaHR0cHM6Ly9naXRodWIuY29tL0dpdHViVXNlck5hbWUvcmVwb3NpdG9yeS1uYW1lKScpO1xuICAgICAgICAgICAgICAgICAgICB0ZXh0RWwub25DaGFuZ2UoKHZhbHVlKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgICAgICB0aGlzLmFkZHJlc3MgPSB2YWx1ZS50cmltKCk7XG4gICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICB0ZXh0RWwuaW5wdXRFbC5hZGRFdmVudExpc3RlbmVyKCdrZXlkb3duJywgYXN5bmMgKGU6IEtleWJvYXJkRXZlbnQpID0+IHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGlmIChlLmtleSA9PT0gJ0VudGVyJyAmJiB0aGlzLmFkZHJlc3MgIT09ICcgJykge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIChcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKHRoaXMudXNlRnJvemVuVmVyc2lvbiAmJiB0aGlzLnZlcnNpb24gIT09IFwiXCIpIFxuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICB8fCAoIXRoaXMudXNlRnJvemVuVmVyc2lvbilcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICApIHtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZS5wcmV2ZW50RGVmYXVsdCgpO1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBhd2FpdCB0aGlzLnN1Ym1pdEZvcm0oKTtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICB0ZXh0RWwuaW5wdXRFbC5zdHlsZS53aWR0aCA9IFwiMTAwJVwiO1xuICAgICAgICAgICAgICAgIH0pO1xuXG4gICAgICAgICAgICBpZiAodGhpcy51c2VGcm96ZW5WZXJzaW9uKSB7XG4gICAgICAgICAgICAgICAgbmV3IFNldHRpbmcoZm9ybUVsKVxuICAgICAgICAgICAgICAgICAgICAuYWRkVGV4dCgodGV4dEVsKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgICAgICB0ZXh0RWwuc2V0UGxhY2Vob2xkZXIoJ1NwZWNpZnkgdGhlIHJlbGVhc2UgdmVyc2lvbiB0YWcgKGV4YW1wbGU6IDEuMC4wKScpO1xuICAgICAgICAgICAgICAgICAgICAgICAgdGV4dEVsLm9uQ2hhbmdlKCh2YWx1ZSkgPT4ge1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRoaXMudmVyc2lvbiA9IHZhbHVlLnRyaW0oKTtcbiAgICAgICAgICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgICAgICAgICAgICAgdGV4dEVsLmlucHV0RWwuc3R5bGUud2lkdGggPSBcIjEwMCVcIjtcbiAgICAgICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9XG5cbiAgICAgICAgICAgIGZvcm1FbC5jcmVhdGVEaXYoJ21vZGFsLWJ1dHRvbi1jb250YWluZXInLCAoYnV0dG9uQ29udGFpbmVyRWwpID0+IHtcbiAgICAgICAgICAgICAgICBidXR0b25Db250YWluZXJFbFxuICAgICAgICAgICAgICAgICAgICAuY3JlYXRlRWwoJ2J1dHRvbicsIHsgYXR0cjogeyB0eXBlOiAnYnV0dG9uJyB9LCB0ZXh0OiAnTmV2ZXIgbWluZCcgfSlcbiAgICAgICAgICAgICAgICAgICAgLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4gdGhpcy5jbG9zZSgpKTtcbiAgICAgICAgICAgICAgICBidXR0b25Db250YWluZXJFbC5jcmVhdGVFbCgnYnV0dG9uJywge1xuICAgICAgICAgICAgICAgICAgICBhdHRyOiB7IHR5cGU6ICdzdWJtaXQnIH0sXG4gICAgICAgICAgICAgICAgICAgIGNsczogJ21vZC1jdGEnLFxuICAgICAgICAgICAgICAgICAgICB0ZXh0OiAnQWRkIFBsdWdpbicsXG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9KTtcblxuICAgICAgICAgICAgY29uc3QgbmV3RGl2ID0gZm9ybUVsLmNyZWF0ZURpdigpO1xuICAgICAgICAgICAgbmV3RGl2LnN0eWxlLmJvcmRlclRvcCA9IFwiMXB4IHNvbGlkICNjY2NcIjtcbiAgICAgICAgICAgIG5ld0Rpdi5zdHlsZS5tYXJnaW5Ub3AgPSBcIjMwcHhcIjtcbiAgICAgICAgICAgIGNvbnN0IGJ5VGZUaGFja2VyID0gbmV3RGl2LmNyZWF0ZVNwYW4oKTtcbiAgICAgICAgICAgIGJ5VGZUaGFja2VyLmlubmVySFRNTCA9IFwiQlJBVCBieSA8YSBocmVmPSdodHRwczovL2JpdC5seS9vNDItdHdpdHRlcic+VEZUSGFja2VyPC9hPlwiO1xuICAgICAgICAgICAgYnlUZlRoYWNrZXIuc3R5bGUuZm9udFN0eWxlID0gXCJpdGFsaWNcIjtcbiAgICAgICAgICAgIG5ld0Rpdi5hcHBlbmRDaGlsZChieVRmVGhhY2tlcik7XG4gICAgICAgICAgICBwcm9tb3Rpb25hbExpbmtzKG5ld0RpdiwgZmFsc2UpO1xuXG4gICAgICAgICAgICB3aW5kb3cuc2V0VGltZW91dCgoKSA9PiB7XG4gICAgICAgICAgICAgICAgY29uc3QgdGl0bGUgPSBmb3JtRWwucXVlcnlTZWxlY3RvckFsbChcIi5icmF0LW1vZGFsIC5zZXR0aW5nLWl0ZW0taW5mb1wiKTtcbiAgICAgICAgICAgICAgICB0aXRsZS5mb3JFYWNoKCh0aXRsZUVsKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHRpdGxlRWwucmVtb3ZlKCk7XG4gICAgICAgICAgICAgICAgfSlcbiAgICAgICAgICAgIH0sIDUwKVxuXG5cbiAgICAgICAgICAgIC8vIGludm9rZWQgd2hlbiBidXR0b24gaXMgY2xpY2tlZC4gXG4gICAgICAgICAgICBmb3JtRWwuYWRkRXZlbnRMaXN0ZW5lcignc3VibWl0JywgYXN5bmMgKGU6IEV2ZW50KSA9PiB7XG4gICAgICAgICAgICAgICAgZS5wcmV2ZW50RGVmYXVsdCgpO1xuICAgICAgICAgICAgICAgIGlmICh0aGlzLmFkZHJlc3MgIT09ICcnKSB7XG4gICAgICAgICAgICAgICAgICAgIGlmIChcbiAgICAgICAgICAgICAgICAgICAgICAgICh0aGlzLnVzZUZyb3plblZlcnNpb24gJiYgdGhpcy52ZXJzaW9uICE9PSBcIlwiKSBcbiAgICAgICAgICAgICAgICAgICAgICAgIHx8ICghdGhpcy51c2VGcm96ZW5WZXJzaW9uKVxuICAgICAgICAgICAgICAgICAgICApIHtcbiAgICAgICAgICAgICAgICAgICAgICAgIGF3YWl0IHRoaXMuc3VibWl0Rm9ybSgpO1xuICAgICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfSk7XG4gICAgICAgIH0pO1xuICAgIH1cbiAgICBcbiAgICBhc3luYyBvbkNsb3NlKCk6IFByb21pc2U8dm9pZD4ge1xuICAgICAgICBpZih0aGlzLm9wZW5TZXR0aW5nc1RhYkFmdGVyd2FyZHMpIHtcbiAgICAgICAgICAgIGF3YWl0ICh0aGlzLnBsdWdpbiBhcyBhbnkpLmFwcC5zZXR0aW5nLm9wZW4oKTtcbiAgICAgICAgICAgIGF3YWl0ICh0aGlzLnBsdWdpbiBhcyBhbnkpLmFwcC5zZXR0aW5nLm9wZW5UYWJCeUlkKFwib2JzaWRpYW40Mi1icmF0XCIpO1xuICAgICAgICB9XG5cbiAgICB9XG59IiwgImltcG9ydCBUaGVQbHVnaW4gZnJvbSBcIi4uL21haW5cIjtcbmltcG9ydCBBZGROZXdQbHVnaW5Nb2RhbCBmcm9tIFwiLi4vdWkvQWRkTmV3UGx1Z2luTW9kYWxcIjtcbmltcG9ydCB7IGdyYWJNYW5pZmVzdEpzb25Gcm9tUmVwb3NpdG9yeSwgZ3JhYlJlbGVhc2VGaWxlRnJvbVJlcG9zaXRvcnkgfSBmcm9tIFwiLi9naXRodWJVdGlsc1wiO1xuaW1wb3J0IHsgbm9ybWFsaXplUGF0aCwgUGx1Z2luTWFuaWZlc3QsIE5vdGljZSwgcmVxdWlyZUFwaVZlcnNpb24sIGFwaVZlcnNpb24gfSBmcm9tIFwib2JzaWRpYW5cIjtcbmltcG9ydCB7IGFkZEJldGFQbHVnaW5Ub0xpc3QgfSBmcm9tIFwiLi4vdWkvc2V0dGluZ3NcIjtcbmltcG9ydCB7IFRvYXN0TWVzc2FnZSB9IGZyb20gXCIuLi91dGlscy9ub3RpZmljYXRpb25zXCI7XG5pbXBvcnQgeyBpc0Nvbm5lY3RlZFRvSW50ZXJuZXQgfSBmcm9tIFwiLi4vdXRpbHMvaW50ZXJuZXRjb25uZWN0aW9uXCI7XG5cbi8qKlxuICogYWxsIHRoZSBmaWxlcyBuZWVkZWQgZm9yIGEgcGx1Z2luIGJhc2VkIG9uIHRoZSByZWxlYXNlIGZpbGVzIGFyZSBocmVcbiAqL1xuaW50ZXJmYWNlIFJlbGVhc2VGaWxlcyB7XG4gICAgbWFpbkpzOiAgICAgc3RyaW5nIHwgbnVsbDtcbiAgICBtYW5pZmVzdDogICBzdHJpbmcgfCBudWxsO1xuICAgIHN0eWxlczogICAgIHN0cmluZyB8IG51bGw7XG59XG5cbi8qKlxuICogUHJpbWFyeSBoYW5kbGVyIGZvciBhZGRpbmcsIHVwZGF0aW5nLCBkZWxldGluZyBiZXRhIHBsdWdpbnMgdHJhY2tlZCBieSB0aGlzIHBsdWdpblxuICovXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBCZXRhUGx1Z2lucyB7XG4gICAgcGx1Z2luOiBUaGVQbHVnaW47XG5cbiAgICBjb25zdHJ1Y3RvcihwbHVnaW46IFRoZVBsdWdpbikge1xuICAgICAgICB0aGlzLnBsdWdpbiA9IHBsdWdpbjtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBvcGVucyB0aGUgQWRkTmV3UGx1Z2luTW9kYWwgdG8gZ2V0IGluZm8gZm9yICBhIG5ldyBiZXRhIHBsdWdpblxuICAgICAqIEBwYXJhbSAgIHtib29sZWFufSAgIG9wZW5TZXR0aW5nc1RhYkFmdGVyd2FyZHMgd2lsbCBvcGVuIHNldHRpbmdzIHNjcmVlbiBhZnRlcndhcmRzLiBVc2VkIHdoZW4gdGhpcyBjb21tYW5kIGlzIGNhbGxlZCBmcm9tIHNldHRpbmdzIHRhYlxuICAgICAqIEBwYXJhbSAgIHtib29sZWFufSAgIHVzZUZyb3plblZlcnNpb24gICAgICAgICAgaW5zdGFsbCB0aGUgcGx1Z2luIHVzaW5nIGZyb3plbiB2ZXJzaW9uLlxuICAgICAqIEByZXR1cm4gIHs8UHJvbWlzZT48dm9pZD59XG4gICAgICovXG4gICAgYXN5bmMgZGlzcGxheUFkZE5ld1BsdWdpbk1vZGFsKG9wZW5TZXR0aW5nc1RhYkFmdGVyd2FyZHMgPSBmYWxzZSwgdXNlRnJvemVuVmVyc2lvbiA9IGZhbHNlKTogUHJvbWlzZTx2b2lkPiB7XG4gICAgICAgIGNvbnN0IG5ld1BsdWdpbiA9IG5ldyBBZGROZXdQbHVnaW5Nb2RhbCh0aGlzLnBsdWdpbiwgdGhpcywgb3BlblNldHRpbmdzVGFiQWZ0ZXJ3YXJkcywgdXNlRnJvemVuVmVyc2lvbik7XG4gICAgICAgIG5ld1BsdWdpbi5vcGVuKCk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogVmFsaWRhdGVzIHRoYXQgYSBHaXRIdWIgcmVwb3NpdG9yeSBpcyBwbHVnaW5cbiAgICAgKlxuICAgICAqIEBwYXJhbSAgIHtzdHJpbmd9ICAgICAgICAgICAgICAgICAgICAgcmVwb3NpdG9yeVBhdGggICBHaXRodWJVc2VyL1JlcG9zaXRvcnlOYW1lIChleGFtcGxlOiBUZlRoYWNrZXIvb2JzaWRpYW40Mi1icmF0KVxuICAgICAqIEBwYXJhbSAgIHtbdHlwZV19ICAgICAgICAgICAgICAgICAgICAgZ2V0QmV0YU1hbmlmZXN0ICB0ZXN0IHRoZSBiZXRhIHZlcnNpb24gb2YgdGhlIG1hbmlmZXN0LCBub3QgYXQgdGhlIHJvb3RcbiAgICAgKiBAcGFyYW0gICB7W3R5cGVdfSAgICAgICAgICAgICAgICAgICAgIGZhbHNlICAgICAgICAgICAgW2ZhbHNlIGRlc2NyaXB0aW9uXVxuICAgICAqIEBwYXJhbSAgIHtbdHlwZV19ICAgICAgICAgICAgICAgICAgICAgcmVwb3J0SXNzdWVzICAgICAgd2lsbCBkaXNwbGF5IG5vdGljZXMgYXMgaXQgZmluZHMgaXNzdWVzXG4gICAgICpcbiAgICAgKiBAcmV0dXJuICB7UHJvbWlzZTxQbHVnaW5NYW5pZmVzdD59ICAgICAgICAgICAgICAgICAgICAgdGhlIG1hbmlmZXN0IGZpbGUgaWYgZm91bmQsIG9yIG51bGwgaWYgaXRzIGluY29tcGxldGVcbiAgICAgKi9cbiAgICBhc3luYyB2YWxpZGF0ZVJlcG9zaXRvcnkocmVwb3NpdG9yeVBhdGg6IHN0cmluZywgZ2V0QmV0YU1hbmlmZXN0ID0gZmFsc2UsIHJlcG9ydElzc3VlcyA9IGZhbHNlKTogUHJvbWlzZTxQbHVnaW5NYW5pZmVzdHxudWxsPiB7XG4gICAgICAgIGNvbnN0IG5vdGljZVRpbWVvdXQgPSAxNTtcbiAgICAgICAgY29uc3QgbWFuaWZlc3RKc29uID0gYXdhaXQgZ3JhYk1hbmlmZXN0SnNvbkZyb21SZXBvc2l0b3J5KHJlcG9zaXRvcnlQYXRoLCAhZ2V0QmV0YU1hbmlmZXN0LCB0aGlzLnBsdWdpbi5zZXR0aW5ncy5kZWJ1Z2dpbmdNb2RlKTtcbiAgICAgICAgaWYgKCFtYW5pZmVzdEpzb24pIHsgLy8gdGhpcyBpcyBhIHBsdWdpbiB3aXRoIGEgbWFuaWZlc3QganNvbiwgdHJ5IHRvIHNlZSBpZiB0aGVyZSBpcyBhIGJldGEgdmVyc2lvblxuICAgICAgICAgICAgaWYgKHJlcG9ydElzc3VlcykgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBgJHtyZXBvc2l0b3J5UGF0aH1cXG5UaGlzIGRvZXMgbm90IHNlZW0gdG8gYmUgYW4gb2JzaWRpYW4gcGx1Z2luLCBhcyB0aGVyZSBpcyBubyBtYW5pZmVzdC5qc29uIGZpbGUuYCwgbm90aWNlVGltZW91dCk7XG4gICAgICAgICAgICByZXR1cm4gbnVsbDtcbiAgICAgICAgfVxuICAgICAgICAvLyBUZXN0IHRoYXQgdGhlIG1haW5mZXN0IGhhcyBzb21lIGtleSBlbGVtZW50cywgbGlrZSBJRCBhbmQgdmVyc2lvblxuICAgICAgICBpZiAoIShcImlkXCIgaW4gbWFuaWZlc3RKc29uKSkgeyAvLyB0aGlzIGlzIGEgcGx1Z2luIHdpdGggYSBtYW5pZmVzdCBqc29uLCB0cnkgdG8gc2VlIGlmIHRoZXJlIGlzIGEgYmV0YSB2ZXJzaW9uXG4gICAgICAgICAgICBpZiAocmVwb3J0SXNzdWVzKSBUb2FzdE1lc3NhZ2UodGhpcy5wbHVnaW4sYCR7cmVwb3NpdG9yeVBhdGh9XFxuVGhlIHBsdWdpbiBpZCBhdHRyaWJ1dGUgZm9yIHRoZSByZWxlYXNlIGlzIG1pc3NpbmcgZnJvbSB0aGUgbWFuaWZlc3QgZmlsZWAsIG5vdGljZVRpbWVvdXQpO1xuICAgICAgICAgICAgcmV0dXJuIG51bGw7XG4gICAgICAgIH1cbiAgICAgICAgaWYgKCEoXCJ2ZXJzaW9uXCIgaW4gbWFuaWZlc3RKc29uKSkgeyAvLyB0aGlzIGlzIGEgcGx1Z2luIHdpdGggYSBtYW5pZmVzdCBqc29uLCB0cnkgdG8gc2VlIGlmIHRoZXJlIGlzIGEgYmV0YSB2ZXJzaW9uXG4gICAgICAgICAgICBpZiAocmVwb3J0SXNzdWVzKSBUb2FzdE1lc3NhZ2UodGhpcy5wbHVnaW4sYCR7cmVwb3NpdG9yeVBhdGh9XFxuVGhlIHZlcnNpb24gYXR0cmlidXRlIGZvciB0aGUgcmVsZWFzZSBpcyBtaXNzaW5nIGZyb20gdGhlIG1hbmlmZXN0IGZpbGVgLCBub3RpY2VUaW1lb3V0KTtcbiAgICAgICAgICAgIHJldHVybiBudWxsO1xuICAgICAgICB9XG4gICAgICAgIHJldHVybiBtYW5pZmVzdEpzb247XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogR2V0cyBhbGwgdGhlIHJlbGVhc2UgZmlsZXMgYmFzZWQgb24gdGhlIHZlcnNpb24gbnVtYmVyIGluIHRoZSBtYW5pZmVzdFxuICAgICAqXG4gICAgICogQHBhcmFtICAge3N0cmluZ30gICAgICAgICAgICAgICAgICAgICAgICByZXBvc2l0b3J5UGF0aCAgcGF0aCB0byB0aGUgR2l0SHViIHJlcG9zaXRvcnlcbiAgICAgKiBAcGFyYW0gICB7UGx1Z2luTWFuaWZlc3Q8UmVsZWFzZUZpbGVzPn0gIG1hbmlmZXN0ICAgICAgICBtYW5pZmVzdCBmaWxlXG4gICAgICogQHBhcmFtICAge2Jvb2xlYW59ICAgICAgICAgICAgICAgICAgICAgICBnZXRNYW5pZmVzdCAgICAgZ3JhYiB0aGUgcmVtb3RlIG1hbmlmZXN0IGZpbGVcbiAgICAgKiBAcGFyYW0gICB7c3RyaW5nfSAgICAgICAgICAgICAgICAgICAgICAgIHNwZWNpZnlWZXJzaW9uICBncmFiIHRoZSBzcGVjaWZpZWQgdmVyc2lvbiBpZiBzZXRcbiAgICAgKlxuICAgICAqIEByZXR1cm4gIHtQcm9taXNlPFJlbGVhc2VGaWxlcz59ICAgICAgICAgICAgICAgICAgICAgICAgIGFsbCByZWxhc2UgZmlsZXMgYXMgc3RyaW5ncyBiYXNlZCBvbiB0aGUgUmVsZWFzZUZpbGVzIGludGVyYWZhY2VcbiAgICAgKi9cbiAgICBhc3luYyBnZXRBbGxSZWxlYXNlRmlsZXMocmVwb3NpdG9yeVBhdGg6IHN0cmluZywgbWFuaWZlc3Q6IFBsdWdpbk1hbmlmZXN0LCBnZXRNYW5pZmVzdDogYm9vbGVhbiwgc3BlY2lmeVZlcnNpb24gPSBcIlwiKTogUHJvbWlzZTxSZWxlYXNlRmlsZXM+IHtcbiAgICAgICAgY29uc3QgdmVyc2lvbiA9IHNwZWNpZnlWZXJzaW9uID09PSBcIlwiID8gbWFuaWZlc3QudmVyc2lvbiA6IHNwZWNpZnlWZXJzaW9uO1xuXG4gICAgICAgIC8vIGlmIHdlIGhhdmUgdmVyc2lvbiBzcGVjaWZpZWQsIHdlIGFsd2F5cyB3YW50IHRvIGdldCB0aGUgcmVtb3RlIG1hbmlmZXN0IGZpbGUuXG4gICAgICAgIGNvbnN0IHJlYWxseUdldE1hbmlmZXN0T3JOb3QgPSBnZXRNYW5pZmVzdCB8fCAoc3BlY2lmeVZlcnNpb24gIT09IFwiXCIpO1xuXG4gICAgICAgIHJldHVybiB7XG4gICAgICAgICAgICBtYWluSnM6IGF3YWl0IGdyYWJSZWxlYXNlRmlsZUZyb21SZXBvc2l0b3J5KHJlcG9zaXRvcnlQYXRoLCB2ZXJzaW9uLCBcIm1haW4uanNcIiwgdGhpcy5wbHVnaW4uc2V0dGluZ3MuZGVidWdnaW5nTW9kZSksXG4gICAgICAgICAgICBtYW5pZmVzdDogcmVhbGx5R2V0TWFuaWZlc3RPck5vdCA/IGF3YWl0IGdyYWJSZWxlYXNlRmlsZUZyb21SZXBvc2l0b3J5KHJlcG9zaXRvcnlQYXRoLCB2ZXJzaW9uLCBcIm1hbmlmZXN0Lmpzb25cIiwgdGhpcy5wbHVnaW4uc2V0dGluZ3MuZGVidWdnaW5nTW9kZSkgOiBcIlwiLFxuICAgICAgICAgICAgc3R5bGVzOiBhd2FpdCBncmFiUmVsZWFzZUZpbGVGcm9tUmVwb3NpdG9yeShyZXBvc2l0b3J5UGF0aCwgdmVyc2lvbiwgXCJzdHlsZXMuY3NzXCIsIHRoaXMucGx1Z2luLnNldHRpbmdzLmRlYnVnZ2luZ01vZGUpXG4gICAgICAgIH1cbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBXcml0ZXMgdGhlIHBsdWdpbiByZWxlYXNlIGZpbGVzIHRvIHRoZSBsb2NhbCBvYnNpZGlhbiAucGx1Z2lucyBmb2xkZXJcbiAgICAgKlxuICAgICAqIEBwYXJhbSAgIHtzdHJpbmd9ICAgICAgICAgICAgICBiZXRhUGx1Z2luSUQgIHRoZSBpZCBvZiB0aGUgcGx1Z2luIChub3QgdGhlIHJlcG9zaXRvcnkgcGF0aClcbiAgICAgKiBAcGFyYW0gICB7UmVsZWFzZUZpbGVzPHZvaWQ+fSAgcmVsRmlsZXMgICAgICByZWxlYXNlIGZpbGUgYXMgc3RyaW5ncywgYmFzZWQgb24gdGhlIFJlbGVhc2VGaWxlcyBpbnRlcmZhY2VcbiAgICAgKlxuICAgICAqIEByZXR1cm4gIHtQcm9taXNlPHZvaWQ+fSAgICAgICAgICAgICAgICAgICAgIFxuICAgICAqL1xuICAgIGFzeW5jIHdyaXRlUmVsZWFzZUZpbGVzVG9QbHVnaW5Gb2xkZXIoYmV0YVBsdWdpbklEOiBzdHJpbmcsIHJlbEZpbGVzOiBSZWxlYXNlRmlsZXMpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgICAgY29uc3QgcGx1Z2luVGFyZ2V0Rm9sZGVyUGF0aCA9IG5vcm1hbGl6ZVBhdGgodGhpcy5wbHVnaW4uYXBwLnZhdWx0LmNvbmZpZ0RpciArIFwiL3BsdWdpbnMvXCIgKyBiZXRhUGx1Z2luSUQpICsgXCIvXCI7XG4gICAgICAgIGNvbnN0IGFkYXB0ZXIgPSB0aGlzLnBsdWdpbi5hcHAudmF1bHQuYWRhcHRlcjtcbiAgICAgICAgaWYgKGF3YWl0IGFkYXB0ZXIuZXhpc3RzKHBsdWdpblRhcmdldEZvbGRlclBhdGgpID09PSBmYWxzZSB8fFxuICAgICAgICAgICAgIShhd2FpdCBhZGFwdGVyLmV4aXN0cyhwbHVnaW5UYXJnZXRGb2xkZXJQYXRoICsgXCJtYW5pZmVzdC5qc29uXCIpKSkge1xuICAgICAgICAgICAgLy8gaWYgcGx1Z2luIGZvbGRlciBkb2VzbnQgZXhpc3Qgb3IgbWFuaWZlc3QuanNvbiBkb2Vzbid0IGV4aXN0LCBjcmVhdGUgaXQgYW5kIHNhdmUgdGhlIHBsdWdpbiBmaWxlc1xuICAgICAgICAgICAgYXdhaXQgYWRhcHRlci5ta2RpcihwbHVnaW5UYXJnZXRGb2xkZXJQYXRoKTtcbiAgICAgICAgfVxuICAgICAgICBhd2FpdCBhZGFwdGVyLndyaXRlKHBsdWdpblRhcmdldEZvbGRlclBhdGggKyBcIm1haW4uanNcIiwgcmVsRmlsZXMubWFpbkpzISk7XG4gICAgICAgIGF3YWl0IGFkYXB0ZXIud3JpdGUocGx1Z2luVGFyZ2V0Rm9sZGVyUGF0aCArIFwibWFuaWZlc3QuanNvblwiLCByZWxGaWxlcy5tYW5pZmVzdCEpO1xuICAgICAgICBpZiAocmVsRmlsZXMuc3R5bGVzKSBhd2FpdCBhZGFwdGVyLndyaXRlKHBsdWdpblRhcmdldEZvbGRlclBhdGggKyBcInN0eWxlcy5jc3NcIiwgcmVsRmlsZXMuc3R5bGVzKTtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBQcmltYXJ5IGZ1bmN0aW9uIGZvciBhZGRpbmcgYSBuZXcgYmV0YSBwbHVnaW4gdG8gT2JzaWRpYW4uIFxuICAgICAqIEFsc28gdGhpcyBmdW5jdGlvbiBpcyB1c2VkIGZvciB1cGRhdGluZyBleGlzdGluZyBwbHVnaW5zLlxuICAgICAqXG4gICAgICogQHBhcmFtICAge3N0cmluZ30gICAgICAgICAgICAgIHJlcG9zaXRvcnlQYXRoICAgICBwYXRoIHRvIEdpdEh1YiByZXBvc2l0b3J5IGZvcm1hdGVkIGFzIFVTRVJOQU1FL3JlcG9zaXRvcnlcbiAgICAgKiBAcGFyYW0gICB7Ym9vbGVhbn0gICAgICAgICAgICAgdXBkYXRlUGx1Z2luRmlsZXMgIHRydWUgaWYgdGhpcyBpcyBqdXN0IGFuIHVwZGF0ZSBub3QgYW4gaW5zdGFsbFxuICAgICAqIEBwYXJhbSAgIHtib29sZWFufSAgICAgICAgICAgICBzZWVJZlVwZGF0ZWRPbmx5ICAgaWYgdHJ1ZSwgYW5kIHVwZGF0ZVBsdWdpbkZpbGVzIHRydWUsIHdpbGwganVzdCBjaGVjayBmb3IgdXBkYXRlcywgYnV0IG5vdCBkbyB0aGUgdXBkYXRlLiB3aWxsIHJlcG9ydCB0byB1c2VyIHRoYXQgdGhlcmUgaXMgYSBuZXcgcGx1Z2luXG4gICAgICogQHBhcmFtICAge2Jvb2xlYW59ICAgICAgICAgICAgIHJlcG9ydElmTm90VXBkdGVkICBpZiB0cnVlLCByZXBvcnQgaWYgYW4gdXBkYXRlIGhhcyBub3Qgc3VjY2VkXG4gICAgICogQHBhcmFtICAge3N0cmluZ30gICAgICAgICAgICAgIHNwZWNpZnlWZXJzaW9uICAgICBpZiBub3QgZW1wdHksIG5lZWQgdG8gaW5zdGFsbCBhIHNwZWNpZmllZCB2ZXJzaW9uIGluc3RlYWQgb2YgdGhlIHZhbHVlIGluIG1hbmlmZXN0ey1iZXRhfS5qc29uXG4gICAgICogQHBhcmFtICAge2Jvb2xlYW59ICAgICAgICAgICAgIGZvcmNlUmVpbnN0YWxsICAgICBpZiB0cnVlLCB3aWxsIGZvcmNlIGEgcmVpbnN0YWxsIG9mIHRoZSBwbHVnaW4sIGV2ZW4gaWYgaXQgaXMgYWxyZWFkeSBpbnN0YWxsZWRcbiAgICAgKlxuICAgICAqIEByZXR1cm4gIHtQcm9taXNlPGJvb2xlYW4+fSAgICAgICAgICAgICAgICAgICAgICAgdHJ1ZSBpZiBzdWNjZWVkc1xuICAgICAqL1xuICAgIGFzeW5jIGFkZFBsdWdpbihyZXBvc2l0b3J5UGF0aDogc3RyaW5nLCB1cGRhdGVQbHVnaW5GaWxlcyA9IGZhbHNlLCBzZWVJZlVwZGF0ZWRPbmx5ID0gZmFsc2UsIHJlcG9ydElmTm90VXBkdGVkID0gZmFsc2UsIHNwZWNpZnlWZXJzaW9uID0gXCJcIiwgZm9yY2VSZWluc3RhbGwgPSBmYWxzZSApOiBQcm9taXNlPGJvb2xlYW4+IHtcbiAgICAgICAgY29uc3Qgbm90aWNlVGltZW91dCA9IDEwO1xuICAgICAgICBsZXQgcHJpbWFyeU1hbmlmZXN0ID0gYXdhaXQgdGhpcy52YWxpZGF0ZVJlcG9zaXRvcnkocmVwb3NpdG9yeVBhdGgsIHRydWUsIGZhbHNlKTsgLy8gYXR0ZW1wdCB0byBnZXQgbWFuaWZlc3QtYmV0YS5qc29uXG4gICAgICAgIGNvbnN0IHVzaW5nQmV0YU1hbmlmZXN0OiBib29sZWFuID0gcHJpbWFyeU1hbmlmZXN0ID8gdHJ1ZSA6IGZhbHNlO1xuICAgICAgICBpZiAodXNpbmdCZXRhTWFuaWZlc3QgPT09IGZhbHNlKVxuICAgICAgICAgICAgcHJpbWFyeU1hbmlmZXN0ID0gYXdhaXQgdGhpcy52YWxpZGF0ZVJlcG9zaXRvcnkocmVwb3NpdG9yeVBhdGgsIGZhbHNlLCB0cnVlKTsgLy8gYXR0ZW1wdCB0byBnZXQgbWFuaWZlc3QuanNvblxuXG4gICAgICAgIGlmIChwcmltYXJ5TWFuaWZlc3QgPT09IG51bGwpIHtcbiAgICAgICAgICAgIGNvbnN0IG1zZyA9IGAke3JlcG9zaXRvcnlQYXRofVxcbkEgbWFuaWZlc3QuanNvbiBvciBtYW5pZmVzdC1iZXRhLmpzb24gZmlsZSBkb2VzIG5vdCBleGlzdCBpbiB0aGUgcm9vdCBkaXJlY3Rvcnkgb2YgdGhlIHJlcG9zaXRvcnkuIFRoaXMgcGx1Z2luIGNhbm5vdCBiZSBpbnN0YWxsZWQuYDtcbiAgICAgICAgICAgIHRoaXMucGx1Z2luLmxvZyhtc2csIHRydWUpO1xuICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBgJHttc2d9YCwgbm90aWNlVGltZW91dCk7XG4gICAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cblxuICAgICAgICBpZiAoIXByaW1hcnlNYW5pZmVzdC5oYXNPd25Qcm9wZXJ0eSgndmVyc2lvbicpKSB7XG4gICAgICAgICAgICBjb25zdCBtc2cgPSBgJHtyZXBvc2l0b3J5UGF0aH1cXG5UaGUgbWFuaWZlc3Qke3VzaW5nQmV0YU1hbmlmZXN0ID8gXCItYmV0YVwiIDogXCJcIn0uanNvbiBmaWxlIGluIHRoZSByb290IGRpcmVjdG9yeSBvZiB0aGUgcmVwb3NpdG9yeSBkb2VzIG5vdCBoYXZlIGEgdmVyc2lvbiBudW1iZXIgaW4gdGhlIGZpbGUuIFRoaXMgcGx1Z2luIGNhbm5vdCBiZSBpbnN0YWxsZWQuYDtcbiAgICAgICAgICAgIHRoaXMucGx1Z2luLmxvZyhtc2csIHRydWUpO1xuICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBgJHttc2d9YCwgbm90aWNlVGltZW91dCk7XG4gICAgICAgICAgICByZXR1cm4gZmFsc2U7XG4gICAgICAgIH1cblxuICAgICAgICAvLyBDaGVjayBtYW5pZmVzdCBtaW5BcHBWZXJzaW9uIGFuZCBjdXJyZW50IHZlcnNpb24gb2YgT2Jpc2lkYW4sIGRvbid0IGxvYWQgcGx1Z2luIGlmIG5vdCBjb21wYXRpYmxlXG4gICAgICAgIGlmKHByaW1hcnlNYW5pZmVzdC5oYXNPd25Qcm9wZXJ0eSgnbWluQXBwVmVyc2lvbicpKSB7IFxuICAgICAgICAgICAgaWYoICFyZXF1aXJlQXBpVmVyc2lvbihwcmltYXJ5TWFuaWZlc3QubWluQXBwVmVyc2lvbikgKSB7XG4gICAgICAgICAgICAgICAgY29uc3QgbXNnID0gYFBsdWdpbjogJHtyZXBvc2l0b3J5UGF0aH1cXG5cXG5gK1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGBUaGUgbWFuaWZlc3Qke3VzaW5nQmV0YU1hbmlmZXN0ID8gXCItYmV0YVwiIDogXCJcIn0uanNvbiBmb3IgdGhpcyBwbHVnaW4gaW5kaWNhdGVzIHRoYXQgdGhlIE9ic2lkaWFuIGAgK1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGB2ZXJzaW9uIG9mIHRoZSBhcHAgbmVlZHMgdG8gYmUgJHtwcmltYXJ5TWFuaWZlc3QubWluQXBwVmVyc2lvbn0sIGAgK1xuICAgICAgICAgICAgICAgICAgICAgICAgICAgIGBidXQgdGhpcyBpbnN0YWxsYXRpb24gb2YgT2JzaWRpYW4gaXMgJHthcGlWZXJzaW9ufS4gXFxuXFxuWW91IHdpbGwgbmVlZCB0byB1cGRhdGUgeW91ciBgICtcbiAgICAgICAgICAgICAgICAgICAgICAgICAgICBgT2JzaWRpYW4gdG8gdXNlIHRoaXMgcGx1Z2luIG9yIGNvbnRhY3QgdGhlIHBsdWdpbiBkZXZlbG9wZXIgZm9yIG1vcmUgaW5mb3JtYXRpb24uYDtcbiAgICAgICAgICAgICAgICB0aGlzLnBsdWdpbi5sb2cobXNnLCB0cnVlKTtcbiAgICAgICAgICAgICAgICBUb2FzdE1lc3NhZ2UodGhpcy5wbHVnaW4sIGAke21zZ31gLCAzMCk7XG4gICAgICAgICAgICAgICAgcmV0dXJuIGZhbHNlOyAgICBcbiAgICAgICAgICAgIH1cbiAgICAgICAgfVxuXG4gICAgICAgIGNvbnN0IGdldFJlbGVhc2UgPSBhc3luYyAoKSA9PiB7IFxuICAgICAgICAgICAgXG4gICAgICAgICAgICBjb25zdCByRmlsZXMgPSBhd2FpdCB0aGlzLmdldEFsbFJlbGVhc2VGaWxlcyhyZXBvc2l0b3J5UGF0aCwgcHJpbWFyeU1hbmlmZXN0IGFzIFBsdWdpbk1hbmlmZXN0LCB1c2luZ0JldGFNYW5pZmVzdCwgc3BlY2lmeVZlcnNpb24pO1xuICAgICAgICAgICAgaWYgKHVzaW5nQmV0YU1hbmlmZXN0IHx8IHJGaWxlcy5tYW5pZmVzdCA9PT0gXCJcIikgIC8vaWYgYmV0YSwgdXNlIHRoYXQgbWFuaWZlc3QsIG9yIGlmIHRoZXJlIGlzIG5vIG1hbmlmZXN0IGluIHJlbGVhc2UsIHVzZSB0aGUgcHJpbWFyeU1hbmlmZXN0XG4gICAgICAgICAgICAgICAgckZpbGVzLm1hbmlmZXN0ID0gSlNPTi5zdHJpbmdpZnkocHJpbWFyeU1hbmlmZXN0KTtcblxuICAgICAgICAgICAgaWYgKHJGaWxlcy5tYWluSnMgPT09IG51bGwpIHtcbiAgICAgICAgICAgICAgICBjb25zdCBtc2cgPSBgJHtyZXBvc2l0b3J5UGF0aH1cXG5UaGUgcmVsZWFzZSBpcyBub3QgY29tcGxldGUgYW5kIGNhbm5vdCBiZSBkb3dubG9hZC4gbWFpbi5qcyBpcyBtaXNzaW5nIGZyb20gdGhlIFJlbGVhc2VgO1xuICAgICAgICAgICAgICAgIHRoaXMucGx1Z2luLmxvZyhtc2csIHRydWUpO1xuICAgICAgICAgICAgICAgIFRvYXN0TWVzc2FnZSh0aGlzLnBsdWdpbiwgYCR7bXNnfWAsIG5vdGljZVRpbWVvdXQpO1xuICAgICAgICAgICAgICAgIHJldHVybiBudWxsO1xuICAgICAgICAgICAgfVxuICAgICAgICAgICAgcmV0dXJuIHJGaWxlcztcbiAgICAgICAgfVxuXG4gICAgICAgIGlmICh1cGRhdGVQbHVnaW5GaWxlcyA9PT0gZmFsc2UgfHwgZm9yY2VSZWluc3RhbGwgPT09IHRydWUpIHtcbiAgICAgICAgICAgIGNvbnN0IHJlbGVhc2VGaWxlcyA9IGF3YWl0IGdldFJlbGVhc2UoKTtcbiAgICAgICAgICAgIGlmIChyZWxlYXNlRmlsZXMgPT09IG51bGwpIHJldHVybiBmYWxzZTtcbiAgICAgICAgICAgIGF3YWl0IHRoaXMud3JpdGVSZWxlYXNlRmlsZXNUb1BsdWdpbkZvbGRlcihwcmltYXJ5TWFuaWZlc3QuaWQsIHJlbGVhc2VGaWxlcyk7XG4gICAgICAgICAgICBpZihmb3JjZVJlaW5zdGFsbCA9PT0gZmFsc2UpIC8vb25seSBhZGQgdG8gbGlzdCBpZiBub3QgYSBmb3JjZSByZWluc3RhbGxcbiAgICAgICAgICAgICAgICBhd2FpdCBhZGRCZXRhUGx1Z2luVG9MaXN0KHRoaXMucGx1Z2luLCByZXBvc2l0b3J5UGF0aCwgc3BlY2lmeVZlcnNpb24pO1xuICAgICAgICAgICAgLy9AdHMtaWdub3JlXG4gICAgICAgICAgICBhd2FpdCB0aGlzLnBsdWdpbi5hcHAucGx1Z2lucy5sb2FkTWFuaWZlc3RzKCk7XG4gICAgICAgICAgICBpZiAoZm9yY2VSZWluc3RhbGwgPT09IHRydWUpIHtcbiAgICAgICAgICAgICAgICBhd2FpdCB0aGlzLnJlbG9hZFBsdWdpbihwcmltYXJ5TWFuaWZlc3QuaWQpOyAvL3JlbG9hZCBpZiBlbmFibGVkXG4gICAgICAgICAgICAgICAgdGhpcy5wbHVnaW4ubG9nKGAke3JlcG9zaXRvcnlQYXRofSByZWluc3RhbGxlZGAsIHRydWUpO1xuICAgICAgICAgICAgICAgIFRvYXN0TWVzc2FnZSh0aGlzLnBsdWdpbiwgYCR7cmVwb3NpdG9yeVBhdGh9XFxuUGx1Z2luIGhhcyBiZWVuIHJlaW5zdGFsbGVkIGFuZCByZWxvYWRlZC5gLCBub3RpY2VUaW1lb3V0KTtcbiAgICAgICAgICAgIH0gZWxzZSB7XG4gICAgICAgICAgICAgICAgY29uc3QgdmVyc2lvblRleHQgPSBzcGVjaWZ5VmVyc2lvbiA9PT0gXCJcIiA/IFwiXCIgOiBgICh2ZXJzaW9uOiAke3NwZWNpZnlWZXJzaW9ufSlgO1xuICAgICAgICAgICAgICAgIGNvbnN0IG1zZyA9IGAke3JlcG9zaXRvcnlQYXRofSR7dmVyc2lvblRleHR9XFxuVGhlIHBsdWdpbiBoYXMgYmVlbiByZWdpc3RlcmVkIHdpdGggQlJBVC4gWW91IG1heSBzdGlsbCBuZWVkIHRvIGVuYWJsZSBpdCB0aGUgQ29tbXVuaXR5IFBsdWdpbiBMaXN0LmA7XG4gICAgICAgICAgICAgICAgdGhpcy5wbHVnaW4ubG9nKG1zZywgdHJ1ZSk7XG4gICAgICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBtc2csIG5vdGljZVRpbWVvdXQpO1xuICAgICAgICAgICAgfVxuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgLy8gdGVzdCBpZiB0aGUgcGx1Z2luIG5lZWRzIHRvIGJlIHVwZGF0ZWRcbiAgICAgICAgICAgIC8vIGlmIGEgc3BlY2lmaWVkIHZlcnNpb24gaXMgcHJvdmlkZWQsIHRoZW4gd2Ugc2hhbGwgc2tpcCB0aGUgdXBkYXRlXG4gICAgICAgICAgICBjb25zdCBwbHVnaW5UYXJnZXRGb2xkZXJQYXRoID0gdGhpcy5wbHVnaW4uYXBwLnZhdWx0LmNvbmZpZ0RpciArIFwiL3BsdWdpbnMvXCIgKyBwcmltYXJ5TWFuaWZlc3QuaWQgKyBcIi9cIjtcbiAgICAgICAgICAgIGxldCBsb2NhbE1hbmlmZXN0Q29udGVudHMgPSBcIlwiO1xuICAgICAgICAgICAgdHJ5IHtcbiAgICAgICAgICAgICAgICBsb2NhbE1hbmlmZXN0Q29udGVudHMgPSBhd2FpdCB0aGlzLnBsdWdpbi5hcHAudmF1bHQuYWRhcHRlci5yZWFkKHBsdWdpblRhcmdldEZvbGRlclBhdGggKyBcIm1hbmlmZXN0Lmpzb25cIilcbiAgICAgICAgICAgIH0gY2F0Y2ggKGUpIHtcbiAgICAgICAgICAgICAgICBpZiAoZS5lcnJubyA9PT0gLTQwNTggfHwgZS5lcnJubyA9PT0gLTIpIHsgLy8gZmlsZSBkb2VzIG5vdCBleGlzdCwgdHJ5IGluc3RhbGxpbmcgdGhlIHBsdWdpblxuICAgICAgICAgICAgICAgICAgICBhd2FpdCB0aGlzLmFkZFBsdWdpbihyZXBvc2l0b3J5UGF0aCwgZmFsc2UsIHVzaW5nQmV0YU1hbmlmZXN0LCBmYWxzZSwgc3BlY2lmeVZlcnNpb24pO1xuICAgICAgICAgICAgICAgICAgICByZXR1cm4gdHJ1ZTsgLy8gZXZlbiB0aG91Z2ggZmFpbGVkLCByZXR1cm4gdHJ1ZSBzaW5jZSBpbnN0YWxsIHdpbGwgYmUgYXR0ZW1wdGVkXG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgICAgIGVsc2VcbiAgICAgICAgICAgICAgICAgICAgY29uc29sZS5sb2coXCJCUkFUIC0gTG9jYWwgTWFuaWZlc3QgTG9hZFwiLCBwcmltYXJ5TWFuaWZlc3QuaWQsIEpTT04uc3RyaW5naWZ5KGUsIG51bGwsIDIpKTtcbiAgICAgICAgICAgIH1cblxuICAgICAgICAgICAgaWYgKFxuICAgICAgICAgICAgICAgIHNwZWNpZnlWZXJzaW9uICE9PSBcIlwiIFxuICAgICAgICAgICAgICAgIHx8IHRoaXMucGx1Z2luLnNldHRpbmdzLnBsdWdpblN1Ykxpc3RGcm96ZW5WZXJzaW9uLm1hcCh4PT54LnJlcG8pLmluY2x1ZGVzKHJlcG9zaXRvcnlQYXRoKVxuICAgICAgICAgICAgKSB7XG4gICAgICAgICAgICAgICAgLy8gc2tpcCB0aGUgZnJvemVuIHZlcnNpb24gcGx1Z2luXG4gICAgICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBgVGhlIHZlcnNpb24gb2YgJHtyZXBvc2l0b3J5UGF0aH0gaXMgZnJvemVuLCBub3QgdXBkYXRpbmcuYCwgMyk7XG4gICAgICAgICAgICAgICAgcmV0dXJuIGZhbHNlO1xuICAgICAgICAgICAgfVxuXG4gICAgICAgICAgICBjb25zdCBsb2NhbE1hbmlmZXN0SlNPTiA9IGF3YWl0IEpTT04ucGFyc2UobG9jYWxNYW5pZmVzdENvbnRlbnRzKTtcbiAgICAgICAgICAgIGlmIChsb2NhbE1hbmlmZXN0SlNPTi52ZXJzaW9uICE9PSBwcmltYXJ5TWFuaWZlc3QudmVyc2lvbikgeyAvL21hbmlmZXN0IGZpbGVzIGFyZSBub3QgdGhlIHNhbWUsIGRvIGFuIHVwZGF0ZVxuICAgICAgICAgICAgICAgIGNvbnN0IHJlbGVhc2VGaWxlcyA9IGF3YWl0IGdldFJlbGVhc2UoKTtcbiAgICAgICAgICAgICAgICBpZiAocmVsZWFzZUZpbGVzID09PSBudWxsKSByZXR1cm4gZmFsc2U7XG5cbiAgICAgICAgICAgICAgICBpZiAoc2VlSWZVcGRhdGVkT25seSkgeyAvLyBkb250IHVwZGF0ZSwganVzdCByZXBvcnQgaXRcbiAgICAgICAgICAgICAgICAgICAgY29uc3QgbXNnID0gYFRoZXJlIGlzIGFuIHVwZGF0ZSBhdmFpbGFibGUgZm9yICR7cHJpbWFyeU1hbmlmZXN0LmlkfSBmcm9tIHZlcnNpb24gJHtsb2NhbE1hbmlmZXN0SlNPTi52ZXJzaW9ufSB0byAke3ByaW1hcnlNYW5pZmVzdC52ZXJzaW9ufS4gYDtcbiAgICAgICAgICAgICAgICAgICAgdGhpcy5wbHVnaW4ubG9nKG1zZyArIGBbUmVsZWFzZSBJbmZvXShodHRwczovL2dpdGh1Yi5jb20vJHtyZXBvc2l0b3J5UGF0aH0vcmVsZWFzZXMvdGFnLyR7cHJpbWFyeU1hbmlmZXN0LnZlcnNpb259KWAsIGZhbHNlKTtcbiAgICAgICAgICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBtc2csIDMwLCBhc3luYyAoKSA9PiB7IHdpbmRvdy5vcGVuKGBodHRwczovL2dpdGh1Yi5jb20vJHtyZXBvc2l0b3J5UGF0aH0vcmVsZWFzZXMvdGFnLyR7cHJpbWFyeU1hbmlmZXN0IS52ZXJzaW9ufWApfSk7XG4gICAgICAgICAgICAgICAgfSBlbHNlIHtcbiAgICAgICAgICAgICAgICAgICAgYXdhaXQgdGhpcy53cml0ZVJlbGVhc2VGaWxlc1RvUGx1Z2luRm9sZGVyKHByaW1hcnlNYW5pZmVzdC5pZCwgcmVsZWFzZUZpbGVzKTtcbiAgICAgICAgICAgICAgICAgICAgLy9AdHMtaWdub3JlXG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IHRoaXMucGx1Z2luLmFwcC5wbHVnaW5zLmxvYWRNYW5pZmVzdHMoKTtcbiAgICAgICAgICAgICAgICAgICAgLy9AdHMtaWdub3JlXG4gICAgICAgICAgICAgICAgICAgIGlmICh0aGlzLnBsdWdpbi5hcHAucGx1Z2lucy5wbHVnaW5zW3ByaW1hcnlNYW5pZmVzdC5pZF0/Lm1hbmlmZXN0KSBhd2FpdCB0aGlzLnJlbG9hZFBsdWdpbihwcmltYXJ5TWFuaWZlc3QuaWQpOyAvL3JlbG9hZCBpZiBlbmFibGVkXG4gICAgICAgICAgICAgICAgICAgIGNvbnN0IG1zZyA9IGAke3ByaW1hcnlNYW5pZmVzdC5pZH1cXG5QbHVnaW4gaGFzIGJlZW4gdXBkYXRlZCBmcm9tIHZlcnNpb24gJHtsb2NhbE1hbmlmZXN0SlNPTi52ZXJzaW9ufSB0byAke3ByaW1hcnlNYW5pZmVzdC52ZXJzaW9ufS4gYDtcbiAgICAgICAgICAgICAgICAgICAgdGhpcy5wbHVnaW4ubG9nKG1zZyArIGBbUmVsZWFzZSBJbmZvXShodHRwczovL2dpdGh1Yi5jb20vJHtyZXBvc2l0b3J5UGF0aH0vcmVsZWFzZXMvdGFnLyR7cHJpbWFyeU1hbmlmZXN0LnZlcnNpb259KWAsIGZhbHNlKTtcbiAgICAgICAgICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBtc2csIDMwLCBhc3luYyAoKSA9PiB7IHdpbmRvdy5vcGVuKGBodHRwczovL2dpdGh1Yi5jb20vJHtyZXBvc2l0b3J5UGF0aH0vcmVsZWFzZXMvdGFnLyR7cHJpbWFyeU1hbmlmZXN0IS52ZXJzaW9ufWApIH0gKTtcbiAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICB9IGVsc2VcbiAgICAgICAgICAgICAgICBpZiAocmVwb3J0SWZOb3RVcGR0ZWQpIFRvYXN0TWVzc2FnZSh0aGlzLnBsdWdpbiwgYE5vIHVwZGF0ZSBhdmFpbGFibGUgZm9yICR7cmVwb3NpdG9yeVBhdGh9YCwgMyk7XG4gICAgICAgIH1cbiAgICAgICAgcmV0dXJuIHRydWU7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogcmVsb2FkcyBhIHBsdWdpbiAoYXNzdW1pbmcgaXQgaGFzIGJlZW4gZW5hYmxlZCBieSB1c2VyKVxuICAgICAqIHBqZWJ5LCBUaGFua3MgQnJvIGh0dHBzOi8vZ2l0aHViLmNvbS9wamVieS9ob3QtcmVsb2FkL2Jsb2IvbWFzdGVyL21haW4uanNcbiAgICAgKiBcbiAgICAgKiBAcGFyYW0gICB7c3RyaW5nPHZvaWQ+fSAgIHBsdWdpbk5hbWUgIG5hbWUgb2YgcGx1Z2luXG4gICAgICpcbiAgICAgKiBAcmV0dXJuICB7UHJvbWlzZTx2b2lkPn0gICAgICAgICAgICAgIFxuICAgICAqL1xuICAgIGFzeW5jIHJlbG9hZFBsdWdpbihwbHVnaW5OYW1lOiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICBjb25zdCBwbHVnaW5zID0gdGhpcy5wbHVnaW4uYXBwLnBsdWdpbnM7XG4gICAgICAgIHRyeSB7XG4gICAgICAgICAgICBhd2FpdCBwbHVnaW5zLmRpc2FibGVQbHVnaW4ocGx1Z2luTmFtZSk7XG4gICAgICAgICAgICBhd2FpdCBwbHVnaW5zLmVuYWJsZVBsdWdpbihwbHVnaW5OYW1lKTtcbiAgICAgICAgfSBjYXRjaCAoZSkgeyBcbiAgICAgICAgICAgIGlmKHRoaXMucGx1Z2luLnNldHRpbmdzLmRlYnVnZ2luZ01vZGUpXG4gICAgICAgICAgICAgICAgY29uc29sZS5sb2coXCJyZWxvYWQgcGx1Z2luXCIsIGUpIFxuICAgICAgICB9XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogdXBkYXRlcyBhIGJldGEgcGx1Z2luXG4gICAgICpcbiAgICAgKiBAcGFyYW0gICB7c3RyaW5nfSAgIHJlcG9zaXRvcnlQYXRoICByZXBvc2l0b3J5IHBhdGggb24gR2l0SHViXG4gICAgICogQHBhcmFtICAge2Jvb2xlYW59ICBvbmx5Q2hlY2tEb250VXBkYXRlIG9ubHkgbG9va3MgZm9yIHVwZGF0ZVxuICAgICAqXG4gICAgICogQHJldHVybiAge1Byb21pc2U8dm9pZD59ICAgICAgICAgICAgICAgICAgXG4gICAgICovXG4gICAgYXN5bmMgdXBkYXRlUGx1Z2luKHJlcG9zaXRvcnlQYXRoOiBzdHJpbmcsIG9ubHlDaGVja0RvbnRVcGRhdGUgPSBmYWxzZSwgcmVwb3J0SWZOb3RVcGR0ZWQgPSBmYWxzZSwgZm9yY2VSZWluc3RhbGwgPSBmYWxzZSk6IFByb21pc2U8Ym9vbGVhbj4ge1xuICAgICAgICBjb25zdCByZXN1bHQgPSBhd2FpdCB0aGlzLmFkZFBsdWdpbihyZXBvc2l0b3J5UGF0aCwgdHJ1ZSwgb25seUNoZWNrRG9udFVwZGF0ZSwgcmVwb3J0SWZOb3RVcGR0ZWQsIFwiXCIsIGZvcmNlUmVpbnN0YWxsKTtcbiAgICAgICAgaWYgKHJlc3VsdCA9PT0gZmFsc2UgJiYgb25seUNoZWNrRG9udFVwZGF0ZSA9PT0gZmFsc2UpXG4gICAgICAgIFRvYXN0TWVzc2FnZSh0aGlzLnBsdWdpbiwgYCR7cmVwb3NpdG9yeVBhdGh9XFxuVXBkYXRlIG9mIHBsdWdpbiBmYWlsZWQuYClcbiAgICAgICAgcmV0dXJuIHJlc3VsdDtcbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiB3YWxrcyB0aHJvdWdoIHRoZSBsaXN0IG9mIHBsdWdpbnMgd2l0aG91dCBmcm96ZW4gdmVyc2lvbiBhbmQgcGVyZm9ybXMgYW4gdXBkYXRlXG4gICAgICpcbiAgICAgKiBAcGFyYW0gICB7Ym9vbGVhbn0gICAgICAgICAgIHNob3dJbmZvICBzaG91bGQgdGhpcyB3aXRoIGEgc3RhcnRlZC9jb21wbGV0ZWQgbWVzc2FnZSAtIHVzZWZ1bCB3aGVuIHJhbiBmcm9tIENQXG4gICAgICogQHJldHVybiAge1Byb21pc2U8dm9pZD59ICAgICAgICAgICAgICBcbiAgICAgKi9cbiAgICBhc3luYyBjaGVja0ZvclVwZGF0ZXNBbmRJbnN0YWxsVXBkYXRlcyhzaG93SW5mbyA9IGZhbHNlLCBvbmx5Q2hlY2tEb250VXBkYXRlID0gZmFsc2UpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgICAgaWYoYXdhaXQgaXNDb25uZWN0ZWRUb0ludGVybmV0KCk9PT1mYWxzZSkgeyBcbiAgICAgICAgICAgIGNvbnNvbGUubG9nKFwiQlJBVDogTm8gaW50ZXJuZXQgZGV0ZWN0ZWQuXCIpIFxuICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9XG4gICAgICAgIGxldCBuZXdOb3RpY2U6IE5vdGljZTtcbiAgICAgICAgY29uc3QgbXNnMSA9IGBDaGVja2luZyBmb3IgcGx1Z2luIHVwZGF0ZXMgU1RBUlRFRGA7XG4gICAgICAgIHRoaXMucGx1Z2luLmxvZyhtc2cxLCB0cnVlKTtcbiAgICAgICAgaWYgKHNob3dJbmZvICYmIHRoaXMucGx1Z2luLnNldHRpbmdzLm5vdGlmaWNhdGlvbnNFbmFibGVkKSBuZXdOb3RpY2UgPSBuZXcgTm90aWNlKGBCUkFUXFxuJHttc2cxfWAsIDMwMDAwKTtcbiAgICAgICAgY29uc3QgcGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb25OYW1lcyA9IFxuICAgICAgICAgICAgbmV3IFNldCh0aGlzLnBsdWdpbi5zZXR0aW5ncy5wbHVnaW5TdWJMaXN0RnJvemVuVmVyc2lvbi5tYXAoZiA9PiBmLnJlcG8pKTtcbiAgICAgICAgZm9yIChjb25zdCBicCBvZiB0aGlzLnBsdWdpbi5zZXR0aW5ncy5wbHVnaW5MaXN0KSB7XG4gICAgICAgICAgICBpZiAocGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb25OYW1lcy5oYXMoYnApKSB7XG4gICAgICAgICAgICAgICAgY29udGludWU7XG4gICAgICAgICAgICB9XG4gICAgICAgICAgICBhd2FpdCB0aGlzLnVwZGF0ZVBsdWdpbihicCwgb25seUNoZWNrRG9udFVwZGF0ZSk7XG4gICAgICAgIH1cbiAgICAgICAgY29uc3QgbXNnMiA9IGBDaGVja2luZyBmb3IgcGx1Z2luIHVwZGF0ZXMgQ09NUExFVEVEYDtcbiAgICAgICAgdGhpcy5wbHVnaW4ubG9nKG1zZzIsIHRydWUpO1xuICAgICAgICBpZiAoc2hvd0luZm8pIHtcbiAgICAgICAgICAgIG5ld05vdGljZSEuaGlkZSgpO1xuICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBtc2cyLCAxMCk7XG4gICAgICAgIH1cbiAgICB9XG5cbiAgICAvKipcbiAgICAgKiBSZW1vdmVzIHRoZSBiZXRhIHBsdWdpbiBmcm9tIHRoZSBsaXN0IG9mIGJldGEgcGx1Z2lucyAoZG9lcyBub3QgZGVsZXRlIHRoZW0gZnJvbSBkaXNrKVxuICAgICAqXG4gICAgICogQHBhcmFtICAge3N0cmluZzx2b2lkPn0gICBiZXRhUGx1Z2luSUQgIHJlcG9zaXRvcnkgcGF0aFxuICAgICAqXG4gICAgICogQHJldHVybiAge1Byb21pc2U8dm9pZD59ICAgICAgICAgICAgICAgIFtyZXR1cm4gZGVzY3JpcHRpb25dXG4gICAgICovXG4gICAgYXN5bmMgZGVsZXRlUGx1Z2luKHJlcG9zaXRvcnlQYXRoOiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgICAgY29uc3QgbXNnID0gYFJlbW92ZWQgJHtyZXBvc2l0b3J5UGF0aH0gZnJvbSBCUkFUIHBsdWdpbiBsaXN0YDtcbiAgICAgICAgdGhpcy5wbHVnaW4ubG9nKG1zZywgdHJ1ZSk7XG4gICAgICAgIHRoaXMucGx1Z2luLnNldHRpbmdzLnBsdWdpbkxpc3QgPSB0aGlzLnBsdWdpbi5zZXR0aW5ncy5wbHVnaW5MaXN0LmZpbHRlcigoYikgPT4gYiAhPSByZXBvc2l0b3J5UGF0aCk7XG4gICAgICAgIHRoaXMucGx1Z2luLnNldHRpbmdzLnBsdWdpblN1Ykxpc3RGcm96ZW5WZXJzaW9uID0gXG4gICAgICAgICAgICB0aGlzLnBsdWdpbi5zZXR0aW5ncy5wbHVnaW5TdWJMaXN0RnJvemVuVmVyc2lvbi5maWx0ZXIoXG4gICAgICAgICAgICAgICAgKGIpID0+IGIucmVwbyAhPSByZXBvc2l0b3J5UGF0aFxuICAgICAgICAgICAgKTtcbiAgICAgICAgdGhpcy5wbHVnaW4uc2F2ZVNldHRpbmdzKCk7XG4gICAgfVxuXG4gICAgLyoqXG4gICAgICogUmV0dXJucyBhIGxpc3Qgb2YgcGx1Z2lucyB0aGF0IGFyZSBjdXJyZW50bHkgZW5hYmxlZCBvciBjdXJyZW50bHkgZGlzYWJsZWRcbiAgICAgKlxuICAgICAqIEBwYXJhbSAgIHtib29sZWFuW119ICAgICAgICBlbmFibGVkICB0cnVlIGZvciBlbmFibGVkIHBsdWdpbnMsIGZhbHNlIGZvciBkaXNhYmxlZCBwbHV0aW5nc1xuICAgICAqXG4gICAgICogQHJldHVybiAge1BsdWdpbk1hbmlmZXN0W119ICAgICAgICAgICBtYW5pZmVzdHMgIG9mIHBsdWdpbnNcbiAgICAgKi9cbiAgICBnZXRFbmFibGVkRGlzYWJsZWRQbHVnaW5zKGVuYWJsZWQ6IGJvb2xlYW4pOiBQbHVnaW5NYW5pZmVzdFtdIHtcbiAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICBjb25zdCBwbCA9IHRoaXMucGx1Z2luLmFwcC5wbHVnaW5zO1xuICAgICAgICBjb25zdCBtYW5pZmVzdHM6IFBsdWdpbk1hbmlmZXN0W10gPSBPYmplY3QudmFsdWVzKHBsLm1hbmlmZXN0cyk7XG4gICAgICAgIC8vIEB0cy1pZ25vcmVcbiAgICAgICAgY29uc3QgZW5hYmxlZFBsdWdpbnM6IFBsdWdpbk1hbmlmZXN0W10gPSBPYmplY3QudmFsdWVzKHBsLnBsdWdpbnMpLm1hcChwID0+IHAubWFuaWZlc3QpO1xuICAgICAgICByZXR1cm4gZW5hYmxlZCA/XG4gICAgICAgICAgICBtYW5pZmVzdHMuZmlsdGVyKG1hbmlmZXN0ID0+IGVuYWJsZWRQbHVnaW5zLmZpbmQocGx1Z2luTmFtZSA9PiBtYW5pZmVzdC5pZCA9PT0gcGx1Z2luTmFtZS5pZCkpIDpcbiAgICAgICAgICAgIG1hbmlmZXN0cy5maWx0ZXIobWFuaWZlc3QgPT4gIWVuYWJsZWRQbHVnaW5zLmZpbmQocGx1Z2luTmFtZSA9PiBtYW5pZmVzdC5pZCA9PT0gcGx1Z2luTmFtZS5pZCkpO1xuICAgIH1cbn0iLCAiaW1wb3J0IHsgYWRkSWNvbiB9IGZyb20gJ29ic2lkaWFuJztcblxuZXhwb3J0IGZ1bmN0aW9uIGFkZEljb25zKCk6IHZvaWQge1xuICAgIGFkZEljb24oXG4gICAgICAgIFwiQnJhdEljb25cIixcbiAgICAgICAgYDxwYXRoIGZpbGw9XCJjdXJyZW50Q29sb3JcIiBzdHJva2U9XCJjdXJyZW50Q29sb3JcIiAgZD1cIk0gNDEuNjY3OTY5IDQxLjY2Nzk2OSBDIDQxLjY2Nzk2OSAzOS4zNjcxODggMzkuODAwNzgxIDM3LjUgMzcuNSAzNy41IEMgMzUuMTk5MjE5IDM3LjUgMzMuMzMyMDMxIDM5LjM2NzE4OCAzMy4zMzIwMzEgNDEuNjY3OTY5IEMgMzMuMzMyMDMxIDQzLjk2ODc1IDM1LjE5OTIxOSA0NS44MzIwMzEgMzcuNSA0NS44MzIwMzEgQyAzOS44MDA3ODEgNDUuODMyMDMxIDQxLjY2Nzk2OSA0My45Njg3NSA0MS42Njc5NjkgNDEuNjY3OTY5IFogTSA2MC40MTc5NjkgNTguNTgyMDMxIEMgNTkuNDYwOTM4IDU4LjAyMzQzOCA1OC4zMjAzMTIgNTcuODY3MTg4IDU3LjI1IDU4LjE0ODQzOCBDIDU2LjE3OTY4OCA1OC40Mjk2ODggNTUuMjY1NjI1IDU5LjEyNSA1NC43MDcwMzEgNjAuMDgyMDMxIEMgNTMuNzQ2MDk0IDYxLjc3NzM0NCA1MS45NDkyMTkgNjIuODIwMzEyIDUwIDYyLjgyMDMxMiBDIDQ4LjA1MDc4MSA2Mi44MjAzMTIgNDYuMjUzOTA2IDYxLjc3NzM0NCA0NS4yOTI5NjkgNjAuMDgyMDMxIEMgNDQuNzM0Mzc1IDU5LjEyNSA0My44MjAzMTIgNTguNDI5Njg4IDQyLjc1IDU4LjE0ODQzOCBDIDQxLjY3OTY4OCA1Ny44NjcxODggNDAuNTM5MDYyIDU4LjAyMzQzOCAzOS41ODIwMzEgNTguNTgyMDMxIEMgMzcuNTk3NjU2IDU5LjcyNjU2MiAzNi45MTAxNTYgNjIuMjU3ODEyIDM4LjA0Mjk2OSA2NC4yNSBDIDQwLjUgNjguNTMxMjUgNDUuMDYyNSA3MS4xNzE4NzUgNTAgNzEuMTcxODc1IEMgNTQuOTM3NSA3MS4xNzE4NzUgNTkuNSA2OC41MzEyNSA2MS45NTcwMzEgNjQuMjUgQyA2My4wODk4NDQgNjIuMjU3ODEyIDYyLjQwMjM0NCA1OS43MjY1NjIgNjAuNDE3OTY5IDU4LjU4MjAzMSBaIE0gNjIuNSAzNy41IEMgNjAuMTk5MjE5IDM3LjUgNTguMzMyMDMxIDM5LjM2NzE4OCA1OC4zMzIwMzEgNDEuNjY3OTY5IEMgNTguMzMyMDMxIDQzLjk2ODc1IDYwLjE5OTIxOSA0NS44MzIwMzEgNjIuNSA0NS44MzIwMzEgQyA2NC44MDA3ODEgNDUuODMyMDMxIDY2LjY2Nzk2OSA0My45Njg3NSA2Ni42Njc5NjkgNDEuNjY3OTY5IEMgNjYuNjY3OTY5IDM5LjM2NzE4OCA2NC44MDA3ODEgMzcuNSA2Mi41IDM3LjUgWiBNIDUwIDguMzMyMDMxIEMgMjYuOTg4MjgxIDguMzMyMDMxIDguMzMyMDMxIDI2Ljk4ODI4MSA4LjMzMjAzMSA1MCBDIDguMzMyMDMxIDczLjAxMTcxOSAyNi45ODgyODEgOTEuNjY3OTY5IDUwIDkxLjY2Nzk2OSBDIDczLjAxMTcxOSA5MS42Njc5NjkgOTEuNjY3OTY5IDczLjAxMTcxOSA5MS42Njc5NjkgNTAgQyA5MS42Njc5NjkgMjYuOTg4MjgxIDczLjAxMTcxOSA4LjMzMjAzMSA1MCA4LjMzMjAzMSBaIE0gNTAgODMuMzMyMDMxIEMgMzMuOTg4MjgxIDgzLjQwMjM0NCAyMC4xOTE0MDYgNzIuMDc4MTI1IDE3LjEzNjcxOSA1Ni4zNjMyODEgQyAxNC4wNzgxMjUgNDAuNjQ0NTMxIDIyLjYyODkwNiAyNC45NzY1NjIgMzcuNSAxOS4wNDI5NjkgQyAzNy40NTcwMzEgMTkuNjM2NzE5IDM3LjQ1NzAzMSAyMC4yMzgyODEgMzcuNSAyMC44MzIwMzEgQyAzNy41IDI3LjczODI4MSA0My4wOTc2NTYgMzMuMzMyMDMxIDUwIDMzLjMzMjAzMSBDIDUyLjMwMDc4MSAzMy4zMzIwMzEgNTQuMTY3OTY5IDMxLjQ2ODc1IDU0LjE2Nzk2OSAyOS4xNjc5NjkgQyA1NC4xNjc5NjkgMjYuODY3MTg4IDUyLjMwMDc4MSAyNSA1MCAyNSBDIDQ3LjY5OTIxOSAyNSA0NS44MzIwMzEgMjMuMTMyODEyIDQ1LjgzMjAzMSAyMC44MzIwMzEgQyA0NS44MzIwMzEgMTguNTMxMjUgNDcuNjk5MjE5IDE2LjY2Nzk2OSA1MCAxNi42Njc5NjkgQyA2OC40MTAxNTYgMTYuNjY3OTY5IDgzLjMzMjAzMSAzMS41ODk4NDQgODMuMzMyMDMxIDUwIEMgODMuMzMyMDMxIDY4LjQxMDE1NiA2OC40MTAxNTYgODMuMzMyMDMxIDUwIDgzLjMzMjAzMSBaIE0gNTAgODMuMzMyMDMxIFwiIC8+YFxuICAgICk7XG59IiwgImltcG9ydCB7IG1vbWVudCwgVEZpbGUsIFBsYXRmb3JtIH0gZnJvbSBcIm9ic2lkaWFuXCI7XG5pbXBvcnQgeyBnZXREYWlseU5vdGVTZXR0aW5ncyB9IGZyb20gXCJvYnNpZGlhbi1kYWlseS1ub3Rlcy1pbnRlcmZhY2VcIjtcbmltcG9ydCBUaGVQbHVnaW4gZnJvbSBcIi4uL21haW5cIjtcblxuLyoqXG4gKiBMb2dzIGV2ZW50cyB0byBhIGxvZyBmaWxlXG4gKlxuICogQHBhcmFtICAge1RoZVBsdWdpbn0gIHBsdWdpbiAgICAgICAgICAgIFBsdWdpbiBvYmplY3RcbiAqIEBwYXJhbSAgIHtzdHJpbmd9ICAgICB0ZXh0VG9Mb2cgICAgICAgICB0ZXh0IHRvIGJlIHNhdmVkIHRvIGxvZyBmaWxlXG4gKiBAcGFyYW0gICB7W3R5cGVdfSAgICAgdmVyYm9zZUxvZ2dpbmdPbiAgVHJ1ZSBpZiBzaG91bGQgb25seSBiZSBsb2dnZWQgaWYgdmVyYm9zZSBsb2dnaW5nIGlzIGVuYWJsZWRcbiAqXG4gKiBAcmV0dXJuICB7dm9pZH0gICAgICAgICAgICAgICAgICAgICAgICAgXG4gKi9cbmV4cG9ydCBmdW5jdGlvbiBsb2dnZXIocGx1Z2luOiBUaGVQbHVnaW4sIHRleHRUb0xvZzogc3RyaW5nLCB2ZXJib3NlTG9nZ2luZ09uID0gZmFsc2UpOiB2b2lkIHtcbiAgICBpZihwbHVnaW4uc2V0dGluZ3MuZGVidWdnaW5nTW9kZSkgY29uc29sZS5sb2coXCJCUkFUOiBcIiArIHRleHRUb0xvZyk7XG4gICAgaWYgKHBsdWdpbi5zZXR0aW5ncy5sb2dnaW5nRW5hYmxlZCkge1xuICAgICAgICBpZiAocGx1Z2luLnNldHRpbmdzLmxvZ2dpbmdWZXJib3NlRW5hYmxlZCA9PT0gZmFsc2UgJiYgdmVyYm9zZUxvZ2dpbmdPbiA9PT0gdHJ1ZSkge1xuICAgICAgICAgICAgcmV0dXJuO1xuICAgICAgICB9IGVsc2Uge1xuICAgICAgICAgICAgY29uc3QgZmlsZU5hbWUgPSBwbHVnaW4uc2V0dGluZ3MubG9nZ2luZ1BhdGggKyBcIi5tZFwiO1xuICAgICAgICAgICAgY29uc3QgZGF0ZU91dHB1dCA9IFwiW1tcIiArIG1vbWVudCgpLmZvcm1hdChnZXREYWlseU5vdGVTZXR0aW5ncygpLmZvcm1hdCkudG9TdHJpbmcoKSArIFwiXV0gXCIgK1xuICAgICAgICAgICAgICAgIG1vbWVudCgpLmZvcm1hdChcIkhIOm1tXCIpO1xuICAgICAgICAgICAgY29uc3QgbWFjaGluZU5hbWUgPSBQbGF0Zm9ybS5pc0Rlc2t0b3AgPyB3aW5kb3cucmVxdWlyZShcIm9zXCIpLmhvc3RuYW1lKCkgOiBcIk1PQklMRVwiO1xuICAgICAgICAgICAgbGV0IG91dHB1dCA9IGRhdGVPdXRwdXQgKyBcIiBcIiArIG1hY2hpbmVOYW1lICsgXCIgXCIgKyB0ZXh0VG9Mb2cucmVwbGFjZShcIlxcblwiLFwiIFwiKSArIFwiXFxuXFxuXCI7XG4gICAgICAgICAgICBzZXRUaW1lb3V0KGFzeW5jICgpID0+IHtcbiAgICAgICAgICAgICAgICBpZiAoYXdhaXQgcGx1Z2luLmFwcC52YXVsdC5hZGFwdGVyLmV4aXN0cyhmaWxlTmFtZSkgPT09IHRydWUpIHtcbiAgICAgICAgICAgICAgICAgICAgY29uc3QgZmlsZUNvbnRlbnRzID0gYXdhaXQgcGx1Z2luLmFwcC52YXVsdC5hZGFwdGVyLnJlYWQoZmlsZU5hbWUpO1xuICAgICAgICAgICAgICAgICAgICBvdXRwdXQgPSBvdXRwdXQgKyBmaWxlQ29udGVudHM7XG4gICAgICAgICAgICAgICAgICAgIGNvbnN0IGZpbGUgPSBwbHVnaW4uYXBwLnZhdWx0LmdldEFic3RyYWN0RmlsZUJ5UGF0aChmaWxlTmFtZSkgYXMgVEZpbGU7XG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IHBsdWdpbi5hcHAudmF1bHQubW9kaWZ5KGZpbGUsIG91dHB1dCk7XG4gICAgICAgICAgICAgICAgfSBlbHNlXG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IHBsdWdpbi5hcHAudmF1bHQuY3JlYXRlKGZpbGVOYW1lLCBvdXRwdXQpO1xuICAgICAgICAgICAgfSwgMTApO1xuICAgICAgICB9XG4gICAgfVxufSIsICJpbXBvcnQgeyBGdXp6eVN1Z2dlc3RNb2RhbCwgRnV6enlNYXRjaCB9IGZyb20gJ29ic2lkaWFuJztcbmltcG9ydCBUaGVQbHVnaW4gZnJvbSAnLi4vbWFpbic7XG5cbi8qKlxuICogU2ltcGxlIGludGVyZmFjZSBmb3Igd2hhdCBzaG91bGQgYmUgZGlzcGxheWVkIGFuZCBzdG9yZWQgZm9yIHN1Z2dlc3RlclxuICovXG5leHBvcnQgaW50ZXJmYWNlIFN1Z2dlc3Rlckl0ZW0ge1xuICAgIGRpc3BsYXk6IHN0cmluZywgICAgICAgIC8vIGRpc3BsYXllZCB0byB1c2VyXG4gICAgaW5mbzogYW55ICAgICAgICAgICAgICAgLy8gc3VwcGxtZW50YWwgaW5mbyBmb3IgdGhlIGNhbGxiYWNrXG59XG5cbi8qKlxuICogR2VuZXJpYyBzdWdnZXN0ZXIgZm9yIHF1aWNrIHJldXNlXG4gKi9cbmV4cG9ydCBjbGFzcyBHZW5lcmljRnV6enlTdWdnZXN0ZXIgZXh0ZW5kcyBGdXp6eVN1Z2dlc3RNb2RhbDxTdWdnZXN0ZXJJdGVtPntcbiAgICBkYXRhOiBTdWdnZXN0ZXJJdGVtW107XG4gICAgY2FsbGJhY2tGdW5jdGlvbjogYW55O1xuXG4gICAgY29uc3RydWN0b3IocGx1Z2luOiBUaGVQbHVnaW4pIHtcbiAgICAgICAgc3VwZXIocGx1Z2luLmFwcCk7XG4gICAgICAgIHRoaXMuc2NvcGUucmVnaXN0ZXIoW1wiU2hpZnRcIl0sIFwiRW50ZXJcIiwgZXZ0ID0+IHRoaXMuZW50ZXJUcmlnZ2VyKGV2dCkpO1xuICAgICAgICB0aGlzLnNjb3BlLnJlZ2lzdGVyKFtcIkN0cmxcIl0sIFwiRW50ZXJcIiwgZXZ0ID0+IHRoaXMuZW50ZXJUcmlnZ2VyKGV2dCkpO1xuICAgIH1cblxuICAgIHNldFN1Z2dlc3RlckRhdGEoc3VnZ2VzdGVyRGF0YTogQXJyYXk8U3VnZ2VzdGVySXRlbT4pOiB2b2lkIHsgdGhpcy5kYXRhID0gc3VnZ2VzdGVyRGF0YSB9XG5cbiAgICBhc3luYyBkaXNwbGF5KGNhbGxCYWNrOiAoaXRlbTogU3VnZ2VzdGVySXRlbSwgZXZ0OiBNb3VzZUV2ZW50IHwgS2V5Ym9hcmRFdmVudCkgPT4gdm9pZCk6IFByb21pc2U8YW55PiB7XG4gICAgICAgIHRoaXMuY2FsbGJhY2tGdW5jdGlvbiA9IGNhbGxCYWNrO1xuICAgICAgICB0aGlzLm9wZW4oKTtcbiAgICB9XG5cbiAgICBnZXRJdGVtcygpOiBTdWdnZXN0ZXJJdGVtW10geyByZXR1cm4gdGhpcy5kYXRhIH1cblxuICAgIGdldEl0ZW1UZXh0KGl0ZW06IFN1Z2dlc3Rlckl0ZW0pOiBzdHJpbmcgeyByZXR1cm4gaXRlbS5kaXNwbGF5IH1cblxuICAgIG9uQ2hvb3NlSXRlbSgpOiB2b2lkIHsgcmV0dXJuIH0gLy8gcmVxdWlyZWQgYnkgVFMsIGJ1dCBub3QgdXNpbmdcblxuICAgIHJlbmRlclN1Z2dlc3Rpb24oaXRlbTogRnV6enlNYXRjaDxTdWdnZXN0ZXJJdGVtPiwgZWw6IEhUTUxFbGVtZW50KTogdm9pZCB7IGVsLmNyZWF0ZUVsKCdkaXYnLCB7IHRleHQ6IGl0ZW0uaXRlbS5kaXNwbGF5IH0pIH1cblxuICAgIGVudGVyVHJpZ2dlcihldnQ6IEtleWJvYXJkRXZlbnQpOiB2b2lkIHtcbiAgICAgICAgY29uc3Qgc2VsZWN0ZWRUZXh0ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcihcIi5zdWdnZXN0aW9uLWl0ZW0uaXMtc2VsZWN0ZWQgZGl2XCIpIS50ZXh0Q29udGVudDtcbiAgICAgICAgY29uc3QgaXRlbSA9IHRoaXMuZGF0YS5maW5kKGkgPT4gaS5kaXNwbGF5ID09PSBzZWxlY3RlZFRleHQpO1xuICAgICAgICBpZiAoaXRlbSkge1xuICAgICAgICAgICAgdGhpcy5pbnZva2VDYWxsYmFjayhpdGVtLCBldnQpO1xuICAgICAgICAgICAgdGhpcy5jbG9zZSgpO1xuICAgICAgICB9XG4gICAgfVxuXG4gICAgb25DaG9vc2VTdWdnZXN0aW9uKGl0ZW06IEZ1enp5TWF0Y2g8U3VnZ2VzdGVySXRlbT4sIGV2dDogTW91c2VFdmVudCB8IEtleWJvYXJkRXZlbnQpOiB2b2lkIHsgdGhpcy5pbnZva2VDYWxsYmFjayhpdGVtLml0ZW0sIGV2dCkgfVxuXG4gICAgaW52b2tlQ2FsbGJhY2soaXRlbTogU3VnZ2VzdGVySXRlbSwgZXZ0OiBNb3VzZUV2ZW50IHwgS2V5Ym9hcmRFdmVudCk6IHZvaWQgeyB0aGlzLmNhbGxiYWNrRnVuY3Rpb24oaXRlbSwgZXZ0KSB9XG59XG4iLCAiaW1wb3J0IFRoZVBsdWdpbiBmcm9tIFwiLi4vbWFpblwiO1xuaW1wb3J0IHsgR2VuZXJpY0Z1enp5U3VnZ2VzdGVyLCBTdWdnZXN0ZXJJdGVtIH0gZnJvbSBcIi4vR2VuZXJpY0Z1enp5U3VnZ2VzdGVyXCI7XG5pbXBvcnQgeyBncmFiQ29tbW11bml0eVBsdWdpbkxpc3QsIGdyYWJDb21tbXVuaXR5VGhlbWVzTGlzdCB9IGZyb20gXCIuLi9mZWF0dXJlcy9naXRodWJVdGlsc1wiO1xuaW1wb3J0IHsgdGhlbWVzQ2hlY2tBbmRVcGRhdGVzIH0gZnJvbSBcIi4uL2ZlYXR1cmVzL3RoZW1lc1wiO1xuaW1wb3J0IEFkZE5ld1RoZW1lIGZyb20gXCIuL0FkZE5ld1RoZW1lXCI7XG5pbXBvcnQgeyBUb2FzdE1lc3NhZ2UgfSBmcm9tIFwiLi4vdXRpbHMvbm90aWZpY2F0aW9uc1wiO1xuXG5leHBvcnQgZGVmYXVsdCBjbGFzcyBQbHVnaW5Db21tYW5kcyB7XG4gICAgcGx1Z2luOiBUaGVQbHVnaW47XG4gICAgYnJhdENvbW1hbmRzID0gW1xuICAgICAgICB7XG4gICAgICAgICAgICBpZDogXCJCUkFULUFkZEJldGFQbHVnaW5cIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiUGx1Z2luczogQWRkIGEgYmV0YSBwbHVnaW4gZm9yIHRlc3RpbmdcIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogdHJ1ZSxcbiAgICAgICAgICAgIGNhbGxiYWNrOiBhc3luYyAoKSA9PiB7IGF3YWl0IHRoaXMucGx1Z2luLmJldGFQbHVnaW5zLmRpc3BsYXlBZGROZXdQbHVnaW5Nb2RhbChmYWxzZSwgZmFsc2UpIH1cbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgICAgaWQ6IFwiQlJBVC1BZGRCZXRhUGx1Z2luV2l0aEZyb3plblZlcnNpb25cIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiUGx1Z2luczogQWRkIGEgYmV0YSBwbHVnaW4gd2l0aCBmcm96ZW4gdmVyc2lvbiBiYXNlZCBvbiBhIHJlbGVhc2UgdGFnXCIsXG4gICAgICAgICAgICBzaG93SW5SaWJib246IHRydWUsXG4gICAgICAgICAgICBjYWxsYmFjazogYXN5bmMgKCkgPT4geyBhd2FpdCB0aGlzLnBsdWdpbi5iZXRhUGx1Z2lucy5kaXNwbGF5QWRkTmV3UGx1Z2luTW9kYWwoZmFsc2UsIHRydWUpIH1cbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgICAgaWQ6IFwiQlJBVC1jaGVja0ZvclVwZGF0ZXNBbmRVcGRhdGVcIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiUGx1Z2luczogQ2hlY2sgZm9yIHVwZGF0ZXMgdG8gYWxsIGJldGEgcGx1Z2lucyBhbmQgVVBEQVRFXCIsXG4gICAgICAgICAgICBzaG93SW5SaWJib246IHRydWUsXG4gICAgICAgICAgICBjYWxsYmFjazogYXN5bmMgKCkgPT4geyBhd2FpdCB0aGlzLnBsdWdpbi5iZXRhUGx1Z2lucy5jaGVja0ZvclVwZGF0ZXNBbmRJbnN0YWxsVXBkYXRlcyh0cnVlLCBmYWxzZSkgfVxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgICBpZDogXCJCUkFULWNoZWNrRm9yVXBkYXRlc0FuZERvbnRVcGRhdGVcIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiUGx1Z2luczogT25seSBjaGVjayBmb3IgdXBkYXRlcyB0byBiZXRhIHBsdWdpbnMsIGJ1dCBkb24ndCBVcGRhdGVcIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogdHJ1ZSxcbiAgICAgICAgICAgIGNhbGxiYWNrOiBhc3luYyAoKSA9PiB7IGF3YWl0IHRoaXMucGx1Z2luLmJldGFQbHVnaW5zLmNoZWNrRm9yVXBkYXRlc0FuZEluc3RhbGxVcGRhdGVzKHRydWUsIHRydWUpIH1cbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgICAgaWQ6IFwiQlJBVC11cGRhdGVPbmVQbHVnaW5cIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiUGx1Z2luczogQ2hvb3NlIGEgc2luZ2xlIHBsdWdpbiB2ZXJzaW9uIHRvIHVwZGF0ZVwiLFxuICAgICAgICAgICAgc2hvd0luUmliYm9uOiB0cnVlLFxuICAgICAgICAgICAgY2FsbGJhY2s6IGFzeW5jICgpID0+IHtcbiAgICAgICAgICAgICAgICBjb25zdCBwbHVnaW5TdWJMaXN0RnJvemVuVmVyc2lvbk5hbWVzID0gXG4gICAgICAgICAgICAgICAgICAgIG5ldyBTZXQodGhpcy5wbHVnaW4uc2V0dGluZ3MucGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb24ubWFwKGYgPT4gZi5yZXBvKSk7XG4gICAgICAgICAgICAgICAgY29uc3QgcGx1Z2luTGlzdDogU3VnZ2VzdGVySXRlbVtdID0gXG4gICAgICAgICAgICAgICAgICAgIE9iamVjdFxuICAgICAgICAgICAgICAgICAgICAgICAgLnZhbHVlcyh0aGlzLnBsdWdpbi5zZXR0aW5ncy5wbHVnaW5MaXN0KVxuICAgICAgICAgICAgICAgICAgICAgICAgLmZpbHRlcigoZikgPT4gIXBsdWdpblN1Ykxpc3RGcm96ZW5WZXJzaW9uTmFtZXMuaGFzKGYpKVxuICAgICAgICAgICAgICAgICAgICAgICAgLm1hcCgobSkgPT4geyByZXR1cm4geyBkaXNwbGF5OiBtLCBpbmZvOiBtIH0gfSk7XG4gICAgICAgICAgICAgICAgY29uc3QgZ2ZzID0gbmV3IEdlbmVyaWNGdXp6eVN1Z2dlc3Rlcih0aGlzLnBsdWdpbik7XG4gICAgICAgICAgICAgICAgZ2ZzLnNldFN1Z2dlc3RlckRhdGEocGx1Z2luTGlzdCk7XG4gICAgICAgICAgICAgICAgYXdhaXQgZ2ZzLmRpc3BsYXkoYXN5bmMgKHJlc3VsdHMpID0+IHtcbiAgICAgICAgICAgICAgICAgICAgY29uc3QgbXNnID0gYENoZWNraW5nIGZvciB1cGRhdGVzIGZvciAke3Jlc3VsdHMuaW5mb31gO1xuICAgICAgICAgICAgICAgICAgICB0aGlzLnBsdWdpbi5sb2cobXNnLCB0cnVlKTtcbiAgICAgICAgICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBgXFxuJHttc2d9YCwgMyk7XG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IHRoaXMucGx1Z2luLmJldGFQbHVnaW5zLnVwZGF0ZVBsdWdpbihyZXN1bHRzLmluZm8sIGZhbHNlLCB0cnVlKTtcbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgICAgaWQ6IFwiQlJBVC1yZWluc3RhbGxPbmVQbHVnaW5cIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiUGx1Z2luczogQ2hvb3NlIGEgc2luZ2xlIHBsdWdpbiB0byByZWluc3RhbGxcIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogdHJ1ZSxcbiAgICAgICAgICAgIGNhbGxiYWNrOiBhc3luYyAoKSA9PiB7XG4gICAgICAgICAgICAgICAgY29uc3QgcGx1Z2luU3ViTGlzdEZyb3plblZlcnNpb25OYW1lcyA9IFxuICAgICAgICAgICAgICAgICAgICBuZXcgU2V0KHRoaXMucGx1Z2luLnNldHRpbmdzLnBsdWdpblN1Ykxpc3RGcm96ZW5WZXJzaW9uLm1hcChmID0+IGYucmVwbykpO1xuICAgICAgICAgICAgICAgIGNvbnN0IHBsdWdpbkxpc3Q6IFN1Z2dlc3Rlckl0ZW1bXSA9IFxuICAgICAgICAgICAgICAgICAgICBPYmplY3RcbiAgICAgICAgICAgICAgICAgICAgICAgIC52YWx1ZXModGhpcy5wbHVnaW4uc2V0dGluZ3MucGx1Z2luTGlzdClcbiAgICAgICAgICAgICAgICAgICAgICAgIC5maWx0ZXIoKGYpID0+ICFwbHVnaW5TdWJMaXN0RnJvemVuVmVyc2lvbk5hbWVzLmhhcyhmKSlcbiAgICAgICAgICAgICAgICAgICAgICAgIC5tYXAoKG0pID0+IHsgcmV0dXJuIHsgZGlzcGxheTogbSwgaW5mbzogbSB9IH0pO1xuICAgICAgICAgICAgICAgIGNvbnN0IGdmcyA9IG5ldyBHZW5lcmljRnV6enlTdWdnZXN0ZXIodGhpcy5wbHVnaW4pO1xuICAgICAgICAgICAgICAgIGdmcy5zZXRTdWdnZXN0ZXJEYXRhKHBsdWdpbkxpc3QpO1xuICAgICAgICAgICAgICAgIGF3YWl0IGdmcy5kaXNwbGF5KGFzeW5jIChyZXN1bHRzKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIGNvbnN0IG1zZyA9IGBSZWluc3RhbGxpbmcgJHtyZXN1bHRzLmluZm99YDtcbiAgICAgICAgICAgICAgICAgICAgVG9hc3RNZXNzYWdlKHRoaXMucGx1Z2luLCBgXFxuJHttc2d9YCwgMyk7XG4gICAgICAgICAgICAgICAgICAgIHRoaXMucGx1Z2luLmxvZyhtc2csIHRydWUpO1xuICAgICAgICAgICAgICAgICAgICBhd2FpdCB0aGlzLnBsdWdpbi5iZXRhUGx1Z2lucy51cGRhdGVQbHVnaW4ocmVzdWx0cy5pbmZvLCBmYWxzZSwgZmFsc2UsIHRydWUpO1xuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfVxuICAgICAgICB9LCAgICAgICAgXG4gICAgICAgIHtcbiAgICAgICAgICAgIGlkOiBcIkJSQVQtcmVzdGFydFBsdWdpblwiLFxuICAgICAgICAgICAgaWNvbjogXCJCcmF0SWNvblwiLFxuICAgICAgICAgICAgbmFtZTogXCJQbHVnaW5zOiBSZXN0YXJ0IGEgcGx1Z2luIHRoYXQgaXMgYWxyZWFkeSBpbnN0YWxsZWRcIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogdHJ1ZSxcbiAgICAgICAgICAgIGNhbGxiYWNrOiBhc3luYyAoKSA9PiB7XG4gICAgICAgICAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICAgICAgICAgIGNvbnN0IHBsdWdpbkxpc3Q6IFN1Z2dlc3Rlckl0ZW1bXSA9IE9iamVjdC52YWx1ZXModGhpcy5wbHVnaW4uYXBwLnBsdWdpbnMubWFuaWZlc3RzKS5tYXAoKG0pID0+IHsgcmV0dXJuIHsgZGlzcGxheTogbS5pZCwgaW5mbzogbS5pZCB9IH0pO1xuICAgICAgICAgICAgICAgIGNvbnN0IGdmcyA9IG5ldyBHZW5lcmljRnV6enlTdWdnZXN0ZXIodGhpcy5wbHVnaW4pO1xuICAgICAgICAgICAgICAgIGdmcy5zZXRTdWdnZXN0ZXJEYXRhKHBsdWdpbkxpc3QpO1xuICAgICAgICAgICAgICAgIGF3YWl0IGdmcy5kaXNwbGF5KGFzeW5jIChyZXN1bHRzKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIFRvYXN0TWVzc2FnZSh0aGlzLnBsdWdpbiwgYCR7cmVzdWx0cy5pbmZvfVxcblBsdWdpbiByZWxvYWRpbmcgLi4uLi5gLCA1KTtcbiAgICAgICAgICAgICAgICAgICAgYXdhaXQgdGhpcy5wbHVnaW4uYmV0YVBsdWdpbnMucmVsb2FkUGx1Z2luKHJlc3VsdHMuaW5mbyk7XG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9XG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICAgIGlkOiBcIkJSQVQtZGlzYWJsZVBsdWdpblwiLFxuICAgICAgICAgICAgaWNvbjogXCJCcmF0SWNvblwiLFxuICAgICAgICAgICAgbmFtZTogXCJQbHVnaW5zOiBEaXNhYmxlIGEgcGx1Z2luIC0gdG9nZ2xlIGl0IG9mZlwiLFxuICAgICAgICAgICAgc2hvd0luUmliYm9uOiB0cnVlLFxuICAgICAgICAgICAgY2FsbGJhY2s6IGFzeW5jICgpID0+IHtcbiAgICAgICAgICAgICAgICBjb25zdCBwbHVnaW5MaXN0ID0gdGhpcy5wbHVnaW4uYmV0YVBsdWdpbnMuZ2V0RW5hYmxlZERpc2FibGVkUGx1Z2lucyh0cnVlKS5tYXAobWFuaWZlc3QgPT4geyByZXR1cm4geyBkaXNwbGF5OiBgJHttYW5pZmVzdC5uYW1lfSAoJHttYW5pZmVzdC5pZH0pYCwgaW5mbzogbWFuaWZlc3QuaWQgfSB9KTtcbiAgICAgICAgICAgICAgICBjb25zdCBnZnMgPSBuZXcgR2VuZXJpY0Z1enp5U3VnZ2VzdGVyKHRoaXMucGx1Z2luKTtcbiAgICAgICAgICAgICAgICBnZnMuc2V0U3VnZ2VzdGVyRGF0YShwbHVnaW5MaXN0KTtcbiAgICAgICAgICAgICAgICBhd2FpdCBnZnMuZGlzcGxheShhc3luYyAocmVzdWx0cykgPT4ge1xuICAgICAgICAgICAgICAgICAgICB0aGlzLnBsdWdpbi5sb2coYCR7cmVzdWx0cy5kaXNwbGF5fSBwbHVnaW4gZGlzYWJsZWRgLCBmYWxzZSk7XG4gICAgICAgICAgICAgICAgICAgIGlmKHRoaXMucGx1Z2luLnNldHRpbmdzLmRlYnVnZ2luZ01vZGUpIGNvbnNvbGUubG9nKHJlc3VsdHMuaW5mbylcbiAgICAgICAgICAgICAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICAgICAgICAgICAgICBhd2FpdCB0aGlzLnBsdWdpbi5hcHAucGx1Z2lucy5kaXNhYmxlUGx1Z2luQW5kU2F2ZShyZXN1bHRzLmluZm8pO1xuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfVxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgICBpZDogXCJCUkFULWVuYWJsZVBsdWdpblwiLFxuICAgICAgICAgICAgaWNvbjogXCJCcmF0SWNvblwiLFxuICAgICAgICAgICAgbmFtZTogXCJQbHVnaW5zOiBFbmFibGUgYSBwbHVnaW4gLSB0b2dnbGUgaXQgb25cIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogdHJ1ZSxcbiAgICAgICAgICAgIGNhbGxiYWNrOiBhc3luYyAoKSA9PiB7XG4gICAgICAgICAgICAgICAgY29uc3QgcGx1Z2luTGlzdCA9IHRoaXMucGx1Z2luLmJldGFQbHVnaW5zLmdldEVuYWJsZWREaXNhYmxlZFBsdWdpbnMoZmFsc2UpLm1hcChtYW5pZmVzdCA9PiB7IHJldHVybiB7IGRpc3BsYXk6IGAke21hbmlmZXN0Lm5hbWV9ICgke21hbmlmZXN0LmlkfSlgLCBpbmZvOiBtYW5pZmVzdC5pZCB9IH0pO1xuICAgICAgICAgICAgICAgIGNvbnN0IGdmcyA9IG5ldyBHZW5lcmljRnV6enlTdWdnZXN0ZXIodGhpcy5wbHVnaW4pO1xuICAgICAgICAgICAgICAgIGdmcy5zZXRTdWdnZXN0ZXJEYXRhKHBsdWdpbkxpc3QpO1xuICAgICAgICAgICAgICAgIGF3YWl0IGdmcy5kaXNwbGF5KGFzeW5jIChyZXN1bHRzKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHRoaXMucGx1Z2luLmxvZyhgJHtyZXN1bHRzLmRpc3BsYXl9IHBsdWdpbiBlbmFibGVkYCwgZmFsc2UpO1xuICAgICAgICAgICAgICAgICAgICAvLyBAdHMtaWdub3JlXG4gICAgICAgICAgICAgICAgICAgIGF3YWl0IHRoaXMucGx1Z2luLmFwcC5wbHVnaW5zLmVuYWJsZVBsdWdpbkFuZFNhdmUocmVzdWx0cy5pbmZvKTtcbiAgICAgICAgICAgICAgICB9KTtcbiAgICAgICAgICAgIH1cbiAgICAgICAgfSxcbiAgICAgICAge1xuICAgICAgICAgICAgaWQ6IFwiQlJBVC1vcGVuR2l0SHViWlJlcG9zaXRvcnlcIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiUGx1Z2luczogT3BlbiB0aGUgR2l0SHViIHJlcG9zaXRvcnkgZm9yIGEgcGx1Z2luXCIsXG4gICAgICAgICAgICBzaG93SW5SaWJib246IHRydWUsXG4gICAgICAgICAgICBjYWxsYmFjazogYXN5bmMgKCkgPT4ge1xuICAgICAgICAgICAgICAgIGNvbnN0IGNvbW11bml0eVBsdWdpbnMgPSBhd2FpdCBncmFiQ29tbW11bml0eVBsdWdpbkxpc3QodGhpcy5wbHVnaW4uc2V0dGluZ3MuZGVidWdnaW5nTW9kZSk7XG4gICAgICAgICAgICAgICAgY29uc3QgY29tbXVuaXR5UGx1Z2luTGlzdDogU3VnZ2VzdGVySXRlbVtdID0gT2JqZWN0LnZhbHVlcyhjb21tdW5pdHlQbHVnaW5zISkubWFwKChwKSA9PiB7IHJldHVybiB7IGRpc3BsYXk6IGBQbHVnaW46ICR7cC5uYW1lfSAgKCR7cC5yZXBvfSlgLCBpbmZvOiBwLnJlcG8gfSB9KTtcbiAgICAgICAgICAgICAgICBjb25zdCBicmF0TGlzdDogU3VnZ2VzdGVySXRlbVtdID0gT2JqZWN0LnZhbHVlcyh0aGlzLnBsdWdpbi5zZXR0aW5ncy5wbHVnaW5MaXN0KS5tYXAoKHApID0+IHsgcmV0dXJuIHsgZGlzcGxheTogXCJCUkFUOiBcIiArIHAsIGluZm86IHAgfSB9KTtcbiAgICAgICAgICAgICAgICBjb21tdW5pdHlQbHVnaW5MaXN0LmZvckVhY2goc2kgPT4gYnJhdExpc3QucHVzaChzaSkpO1xuICAgICAgICAgICAgICAgIGNvbnN0IGdmcyA9IG5ldyBHZW5lcmljRnV6enlTdWdnZXN0ZXIodGhpcy5wbHVnaW4pO1xuICAgICAgICAgICAgICAgIGdmcy5zZXRTdWdnZXN0ZXJEYXRhKGJyYXRMaXN0KTtcbiAgICAgICAgICAgICAgICBhd2FpdCBnZnMuZGlzcGxheShhc3luYyAocmVzdWx0cykgPT4ge1xuICAgICAgICAgICAgICAgICAgICBpZiAocmVzdWx0cy5pbmZvKSB3aW5kb3cub3BlbihgaHR0cHM6Ly9naXRodWIuY29tLyR7cmVzdWx0cy5pbmZvfWApXG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9XG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICAgIGlkOiBcIkJSQVQtb3BlbkdpdEh1YlJlcG9UaGVtZVwiLFxuICAgICAgICAgICAgaWNvbjogXCJCcmF0SWNvblwiLFxuICAgICAgICAgICAgbmFtZTogXCJUaGVtZXM6IE9wZW4gdGhlIEdpdEh1YiByZXBvc2l0b3J5IGZvciBhIHRoZW1lIChhcHBlYXJhbmNlKVwiLFxuICAgICAgICAgICAgc2hvd0luUmliYm9uOiB0cnVlLFxuICAgICAgICAgICAgY2FsbGJhY2s6IGFzeW5jICgpID0+IHtcbiAgICAgICAgICAgICAgICBjb25zdCBjb21tdW5pdHlUaGVtZSA9IGF3YWl0IGdyYWJDb21tbXVuaXR5VGhlbWVzTGlzdCh0aGlzLnBsdWdpbi5zZXR0aW5ncy5kZWJ1Z2dpbmdNb2RlKTtcbiAgICAgICAgICAgICAgICBjb25zdCBjb21tdW5pdHlUaGVtZUxpc3Q6IFN1Z2dlc3Rlckl0ZW1bXSA9IE9iamVjdC52YWx1ZXMoY29tbXVuaXR5VGhlbWUhKS5tYXAoKHApID0+IHsgcmV0dXJuIHsgZGlzcGxheTogYFRoZW1lOiAke3AubmFtZX0gICgke3AucmVwb30pYCwgaW5mbzogcC5yZXBvIH0gfSk7XG4gICAgICAgICAgICAgICAgY29uc3QgZ2ZzID0gbmV3IEdlbmVyaWNGdXp6eVN1Z2dlc3Rlcih0aGlzLnBsdWdpbik7XG4gICAgICAgICAgICAgICAgZ2ZzLnNldFN1Z2dlc3RlckRhdGEoY29tbXVuaXR5VGhlbWVMaXN0KTtcbiAgICAgICAgICAgICAgICBhd2FpdCBnZnMuZGlzcGxheShhc3luYyAocmVzdWx0cykgPT4ge1xuICAgICAgICAgICAgICAgICAgICBpZiAocmVzdWx0cy5pbmZvKSB3aW5kb3cub3BlbihgaHR0cHM6Ly9naXRodWIuY29tLyR7cmVzdWx0cy5pbmZvfWApXG4gICAgICAgICAgICAgICAgfSk7XG4gICAgICAgICAgICB9XG4gICAgICAgIH0sXG4gICAgICAgIHtcbiAgICAgICAgICAgIGlkOiBcIkJSQVQtb3BlbnRQbHVnaW5TZXR0aW5nc1wiLFxuICAgICAgICAgICAgaWNvbjogXCJCcmF0SWNvblwiLFxuICAgICAgICAgICAgbmFtZTogXCJQbHVnaW5zOiBPcGVuIFBsdWdpbiBTZXR0aW5ncyBUYWJcIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogdHJ1ZSxcbiAgICAgICAgICAgIGNhbGxiYWNrOiBhc3luYyAoKSA9PiB7XG4gICAgICAgICAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICAgICAgICAgIGNvbnN0IHNldHRpbmdzID0gdGhpcy5wbHVnaW4uYXBwLnNldHRpbmc7XG4gICAgICAgICAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICAgICAgICAgIGNvbnN0IGxpc3RPZlBsdWdpblNldHRpbmdzVGFiczogU3VnZ2VzdGVySXRlbVtdID0gT2JqZWN0LnZhbHVlcyhzZXR0aW5ncy5wbHVnaW5UYWJzKS5tYXAoKHQpID0+IHsgcmV0dXJuIHsgZGlzcGxheTogXCJQbHVnaW46IFwiICsgdC5uYW1lLCBpbmZvOiB0LmlkIH0gfSk7XG4gICAgICAgICAgICAgICAgY29uc3QgZ2ZzID0gbmV3IEdlbmVyaWNGdXp6eVN1Z2dlc3Rlcih0aGlzLnBsdWdpbik7XG4gICAgICAgICAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICAgICAgICAgIGNvbnN0IGxpc3RPZkNvcmVTZXR0aW5nc1RhYnM6IFN1Z2dlc3Rlckl0ZW1bXSA9IE9iamVjdC52YWx1ZXMoc2V0dGluZ3Muc2V0dGluZ1RhYnMpLm1hcCgodCkgPT4geyByZXR1cm4geyBkaXNwbGF5OiBcIkNvcmU6IFwiICsgdC5uYW1lLCBpbmZvOiB0LmlkIH0gfSk7XG4gICAgICAgICAgICAgICAgbGlzdE9mUGx1Z2luU2V0dGluZ3NUYWJzLmZvckVhY2goc2kgPT4gbGlzdE9mQ29yZVNldHRpbmdzVGFicy5wdXNoKHNpKSk7XG4gICAgICAgICAgICAgICAgZ2ZzLnNldFN1Z2dlc3RlckRhdGEobGlzdE9mQ29yZVNldHRpbmdzVGFicyk7XG4gICAgICAgICAgICAgICAgYXdhaXQgZ2ZzLmRpc3BsYXkoYXN5bmMgKHJlc3VsdHMpID0+IHtcbiAgICAgICAgICAgICAgICAgICAgc2V0dGluZ3Mub3BlbigpO1xuICAgICAgICAgICAgICAgICAgICBzZXR0aW5ncy5vcGVuVGFiQnlJZChyZXN1bHRzLmluZm8pO1xuICAgICAgICAgICAgICAgIH0pO1xuICAgICAgICAgICAgfVxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgICBpZDogXCJCUkFULUdyYWJCZXRhVGhlbWVcIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiVGhlbWVzOiBHcmFiIGEgYmV0YSB0aGVtZSBmb3IgdGVzdGluZyBmcm9tIGEgR2l0aHViIHJlcG9zaXRvcnlcIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogdHJ1ZSxcbiAgICAgICAgICAgIGNhbGxiYWNrOiBhc3luYyAoKSA9PiB7IChuZXcgQWRkTmV3VGhlbWUodGhpcy5wbHVnaW4pKS5vcGVuKCkgfVxuICAgICAgICB9LFxuICAgICAgICB7XG4gICAgICAgICAgICBpZDogXCJCUkFULXVwZGF0ZUJldGFUaGVtZXNcIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiVGhlbWVzOiBVcGRhdGUgYmV0YSB0aGVtZXNcIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogdHJ1ZSxcbiAgICAgICAgICAgIGNhbGxiYWNrOiBhc3luYyAoKSA9PiBhd2FpdCB0aGVtZXNDaGVja0FuZFVwZGF0ZXModGhpcy5wbHVnaW4sIHRydWUpIFxuICAgICAgICB9LCAgICAgICAgXG4gICAgICAgIHtcbiAgICAgICAgICAgIGlkOiBcIkJSQVQtYWxsQ29tbWFuZHNcIixcbiAgICAgICAgICAgIGljb246IFwiQnJhdEljb25cIixcbiAgICAgICAgICAgIG5hbWU6IFwiQWxsIENvbW1hbmRzIGxpc3RcIixcbiAgICAgICAgICAgIHNob3dJblJpYmJvbjogZmFsc2UsXG4gICAgICAgICAgICBjYWxsYmFjazogYXN5bmMgKCkgPT4gdGhpcy5yaWJib25EaXNwbGF5Q29tbWFuZHMoKVxuICAgICAgICB9LFxuICAgIF1cblxuICAgIGFzeW5jIHJpYmJvbkRpc3BsYXlDb21tYW5kcygpOiBQcm9taXNlPHZvaWQ+IHtcbiAgICAgICAgY29uc3QgYnJhdENvbW1hbmRMaXN0OiBTdWdnZXN0ZXJJdGVtW10gPSBbXTtcbiAgICAgICAgdGhpcy5icmF0Q29tbWFuZHMuZm9yRWFjaChjbWQgPT4geyBpZiAoY21kLnNob3dJblJpYmJvbikgYnJhdENvbW1hbmRMaXN0LnB1c2goeyBkaXNwbGF5OiBjbWQubmFtZSwgaW5mbzogY21kLmNhbGxiYWNrIH0pIH0pO1xuICAgICAgICBjb25zdCBnZnMgPSBuZXcgR2VuZXJpY0Z1enp5U3VnZ2VzdGVyKHRoaXMucGx1Z2luKTtcbiAgICAgICAgLy8gQHRzLWlnbm9yZVxuICAgICAgICBjb25zdCBzZXR0aW5ncyA9IHRoaXMucGx1Z2luLmFwcC5zZXR0aW5nO1xuICAgICAgICAvLyBAdHMtaWdub3JlXG4gICAgICAgIGNvbnN0IGxpc3RPZkNvcmVTZXR0aW5nc1RhYnM6IFN1Z2dlc3Rlckl0ZW1bXSA9IE9iamVjdC52YWx1ZXMoc2V0dGluZ3Muc2V0dGluZ1RhYnMpLm1hcCgodDogYW55KSA9PiB7XG4gICAgICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgICAgIGRpc3BsYXk6IFwiQ29yZTogXCIgKyB0Lm5hbWUsXG4gICAgICAgICAgICAgICAgaW5mbzogYXN5bmMgKCkgPT4ge1xuICAgICAgICAgICAgICAgICAgICBzZXR0aW5ncy5vcGVuKCk7XG4gICAgICAgICAgICAgICAgICAgIHNldHRpbmdzLm9wZW5UYWJCeUlkKHQuaWQpO1xuICAgICAgICAgICAgICAgIH1cbiAgICAgICAgICAgIH1cbiAgICAgICAgfSk7XG4gICAgICAgIC8vIEB0cy1pZ25vcmVcbiAgICAgICAgY29uc3QgbGlzdE9mUGx1Z2luU2V0dGluZ3NUYWJzOiBTdWdnZXN0ZXJJdGVtW10gPSBPYmplY3QudmFsdWVzKHNldHRpbmdzLnBsdWdpblRhYnMpLm1hcCgodDogYW55KSA9PiB7XG4gICAgICAgICAgICByZXR1cm4ge1xuICAgICAgICAgICAgICAgIGRpc3BsYXk6IFwiUGx1Z2luOiBcIiArIHQubmFtZSxcbiAgICAgICAgICAgICAgICBpbmZvOiBhc3luYyAoKSA9PiB7XG4gICAgICAgICAgICAgICAgICAgIHNldHRpbmdzLm9wZW4oKTtcbiAgICAgICAgICAgICAgICAgICAgc2V0dGluZ3Mub3BlblRhYkJ5SWQodC5pZCk7XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICB9KTtcblxuICAgICAgICBicmF0Q29tbWFuZExpc3QucHVzaCh7IGRpc3BsYXk6IFwiLS0tLSBDb3JlIFBsdWdpbiBTZXR0aW5ncyAtLS0tXCIsIGluZm86IGFzeW5jICgpID0+IHsgYXdhaXQgdGhpcy5yaWJib25EaXNwbGF5Q29tbWFuZHMoKSB9IH0pXG4gICAgICAgIGxpc3RPZkNvcmVTZXR0aW5nc1RhYnMuZm9yRWFjaChzaSA9PiBicmF0Q29tbWFuZExpc3QucHVzaChzaSkpO1xuICAgICAgICBicmF0Q29tbWFuZExpc3QucHVzaCh7IGRpc3BsYXk6IFwiLS0tLSBQbHVnaW4gU2V0dGluZ3MgLS0tLVwiLCBpbmZvOiBhc3luYyAoKSA9PiB7IGF3YWl0IHRoaXMucmliYm9uRGlzcGxheUNvbW1hbmRzKCkgfSB9KVxuICAgICAgICBsaXN0T2ZQbHVnaW5TZXR0aW5nc1RhYnMuZm9yRWFjaChzaSA9PiBicmF0Q29tbWFuZExpc3QucHVzaChzaSkpO1xuXG4gICAgICAgIGdmcy5zZXRTdWdnZXN0ZXJEYXRhKGJyYXRDb21tYW5kTGlzdCk7XG4gICAgICAgIGF3YWl0IGdmcy5kaXNwbGF5KGFzeW5jIChyZXN1bHRzKSA9PiBhd2FpdCByZXN1bHRzLmluZm8oKSk7XG4gICAgfVxuXG4gICAgY29uc3RydWN0b3IocGx1Z2luOiBUaGVQbHVnaW4pIHtcbiAgICAgICAgdGhpcy5wbHVnaW4gPSBwbHVnaW47XG5cbiAgICAgICAgdGhpcy5icmF0Q29tbWFuZHMuZm9yRWFjaChhc3luYyAoaXRlbSkgPT4ge1xuICAgICAgICAgICAgdGhpcy5wbHVnaW4uYWRkQ29tbWFuZCh7XG4gICAgICAgICAgICAgICAgaWQ6IGl0ZW0uaWQsXG4gICAgICAgICAgICAgICAgbmFtZTogaXRlbS5uYW1lLFxuICAgICAgICAgICAgICAgIGljb246IGl0ZW0uaWNvbixcbiAgICAgICAgICAgICAgICBjYWxsYmFjazogYXN5bmMgKCkgPT4geyBhd2FpdCBpdGVtLmNhbGxiYWNrKCkgfVxuICAgICAgICAgICAgfSlcbiAgICAgICAgfSk7XG4gICAgfVxuXG59XG5cbiIsICJpbXBvcnQgeyBncmFiQ2hlY2tzdW1PZlRoZW1lQ3NzRmlsZSwgZ3JhYkNvbW1tdW5pdHlUaGVtZUNzc0ZpbGUsIGdyYWJMYXN0Q29tbWl0RGF0ZUZvckFGaWxlIH0gZnJvbSBcIi4uL2ZlYXR1cmVzL2dpdGh1YlV0aWxzXCI7XG5pbXBvcnQgeyB0aGVtZVNhdmUsIHRoZW1lRGVsZXRlLCB0aGVtZXNDaGVja0FuZFVwZGF0ZXMgfSBmcm9tIFwiLi4vZmVhdHVyZXMvdGhlbWVzXCI7XG5pbXBvcnQgVGhlUGx1Z2luIGZyb20gXCIuLi9tYWluXCI7XG5pbXBvcnQgeyBTZXR0aW5ncyB9IGZyb20gXCIuLi91aS9zZXR0aW5nc1wiO1xuXG5cbi8vIFRoaXMgbW9kdWxlIGlzIGZvciBBUEkgYWNjZXNzIGZvciB1c2UgaW4gZGVidWdpbmcgY29uc29sZSBcblxuZXhwb3J0IGRlZmF1bHQgY2xhc3MgQnJhdEFQSSB7XG4gICAgcGx1Z2luOiBUaGVQbHVnaW47XG4gICAgc2V0dGluZ3M6IFNldHRpbmdzOyBcblxuICAgIGNvbnN0cnVjdG9yKHBsdWdpbjogVGhlUGx1Z2luKSB7XG4gICAgICAgIHRoaXMucGx1Z2luID0gcGx1Z2luICAgIFxuICAgIH1cblxuICAgIC8vIGVzbGludC1kaXNhYmxlLW5leHQtbGluZSBAdHlwZXNjcmlwdC1lc2xpbnQvbm8tZXhwbGljaXQtYW55XG4gICAgY29uc29sZSA9IChsb2dEZXNjcmlwdGlvbjogc3RyaW5nLCAuLi5vdXRwdXRzOiBhbnlbXSk6IHZvaWQgPT4ge1xuICAgICAgICBjb25zb2xlLmxvZyhcIkJSQVQ6IFwiICsgbG9nRGVzY3JpcHRpb24sIG91dHB1dHMpXG4gICAgfVxuXG4gICAgdGhlbWVzID0ge1xuXG4gICAgICAgIHRoZW1lc2VDaGVja0FuZFVwYXRlczogYXN5bmMgKHNob3dJbmZvOiBib29sZWFuKTogUHJvbWlzZTx2b2lkPiA9PiB7XG4gICAgICAgICAgICBhd2FpdCB0aGVtZXNDaGVja0FuZFVwZGF0ZXModGhpcy5wbHVnaW4sIHNob3dJbmZvKTtcbiAgICAgICAgfSxcblxuICAgICAgICB0aGVtZUluc3RhbGxUaGVtZTogYXN5bmMgKGNzc0dpdGh1YlJlcG9zaXRvcnk6IHN0cmluZyk6IFByb21pc2U8dm9pZD4gPT4ge1xuICAgICAgICAgICAgY29uc3Qgc2NydWJiZWRBZGRyZXNzID0gY3NzR2l0aHViUmVwb3NpdG9yeS5yZXBsYWNlKFwiaHR0cHM6Ly9naXRodWIuY29tL1wiLCBcIlwiKTtcbiAgICAgICAgICAgIGF3YWl0IHRoZW1lU2F2ZSh0aGlzLnBsdWdpbiwgc2NydWJiZWRBZGRyZXNzLCB0cnVlKTtcbiAgICAgICAgfSxcblxuICAgICAgICB0aGVtZXNEZWxldGU6IGFzeW5jIChjc3NHaXRodWJSZXBvc2l0b3J5OiBzdHJpbmcpOiBQcm9taXNlPHZvaWQ+ID0+IHtcbiAgICAgICAgICAgIGNvbnN0IHNjcnViYmVkQWRkcmVzcyA9IGNzc0dpdGh1YlJlcG9zaXRvcnkucmVwbGFjZShcImh0dHBzOi8vZ2l0aHViLmNvbS9cIiwgXCJcIik7XG4gICAgICAgICAgICBhd2FpdCB0aGVtZURlbGV0ZSh0aGlzLnBsdWdpbiwgc2NydWJiZWRBZGRyZXNzKVxuICAgICAgICB9LFxuXG4gICAgICAgIGdyYWJDb21tbXVuaXR5VGhlbWVDc3NGaWxlOiBhc3luYyAocmVwb3NpdG9yeVBhdGg6IHN0cmluZywgYmV0YVZlcnNpb24gPSBmYWxzZSk6IFByb21pc2U8c3RyaW5nfG51bGw+ID0+ICB7XG4gICAgICAgICAgICByZXR1cm4gYXdhaXQgZ3JhYkNvbW1tdW5pdHlUaGVtZUNzc0ZpbGUocmVwb3NpdG9yeVBhdGgsIGJldGFWZXJzaW9uLCB0aGlzLnBsdWdpbi5zZXR0aW5ncy5kZWJ1Z2dpbmdNb2RlKTtcbiAgICAgICAgfSxcblxuICAgICAgICBncmFiQ2hlY2tzdW1PZlRoZW1lQ3NzRmlsZTogYXN5bmMgKHJlcG9zaXRvcnlQYXRoOiBzdHJpbmcsIGJldGFWZXJzaW9uID0gZmFsc2UpOiBQcm9taXNlPHN0cmluZz4gPT4gIHtcbiAgICAgICAgICAgIHJldHVybiBhd2FpdCBncmFiQ2hlY2tzdW1PZlRoZW1lQ3NzRmlsZShyZXBvc2l0b3J5UGF0aCwgYmV0YVZlcnNpb24sIHRoaXMucGx1Z2luLnNldHRpbmdzLmRlYnVnZ2luZ01vZGUpO1xuICAgICAgICB9LFxuXG4gICAgICAgIGdyYWJMYXN0Q29tbWl0RGF0ZUZvckFGaWxlOiBhc3luYyAocmVwb3NpdG9yeVBhdGg6IHN0cmluZywgcGF0aDogc3RyaW5nKTogUHJvbWlzZTxzdHJpbmc+ID0+IHtcbiAgICAgICAgICAgIC8vIGV4YW1wbGUgYXdhaXQgZ3JhYkxhc3RDb21taXREYXRlRm9yQUZpbGUodC5yZXBvLCBcInRoZW1lLWJldGEuY3NzXCIpO1xuICAgICAgICAgICAgcmV0dXJuIGF3YWl0IGdyYWJMYXN0Q29tbWl0RGF0ZUZvckFGaWxlKHJlcG9zaXRvcnlQYXRoLCBwYXRoKVxuICAgICAgICB9LFxuXG5cblxuXG4gICAgICAgIFxuICAgIH1cblxufSJdLAogICJtYXBwaW5ncyI6ICI7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7Ozs7O0FBQUE7QUFBQTtBQUFBO0FBRUEsV0FBTyxlQUFlLFNBQVMsY0FBYyxFQUFFLE9BQU8sS0FBSyxDQUFDO0FBRTVELFFBQUksV0FBVyxRQUFRLFVBQVU7QUFFakMsUUFBTSw0QkFBNEI7QUFDbEMsUUFBTSw2QkFBNkI7QUFDbkMsUUFBTSw4QkFBOEI7QUFDcEMsUUFBTSxnQ0FBZ0M7QUFDdEMsUUFBTSw2QkFBNkI7QUFFbkMsYUFBUywrQkFBK0IsYUFBYTtBQVpyRDtBQWNJLFlBQU0sZ0JBQWdCLE9BQU8sSUFBSSxRQUFRLFVBQVUsZ0JBQWdCO0FBQ25FLGFBQU8sbUJBQWlCLHlCQUFjLGFBQWQsbUJBQXlCLGlCQUF6QixtQkFBdUM7QUFBQSxJQUNuRTtBQUtBLGFBQVNBLHdCQUF1QjtBQXJCaEM7QUFzQkksVUFBSTtBQUVBLGNBQU0sRUFBRSxpQkFBaUIsUUFBUSxJQUFJLE9BQU87QUFDNUMsWUFBSSwrQkFBK0IsT0FBTyxHQUFHO0FBQ3pDLGdCQUFNLEVBQUUsUUFBQUMsU0FBUSxRQUFBQyxTQUFRLFVBQUFDLFVBQVMsTUFBSSxtQkFBUSxVQUFVLGdCQUFnQixNQUFsQyxtQkFBcUMsYUFBckMsbUJBQStDLFVBQVMsQ0FBQztBQUM5RixpQkFBTztBQUFBLFlBQ0gsUUFBUUYsV0FBVTtBQUFBLFlBQ2xCLFNBQVFDLFdBQUEsZ0JBQUFBLFFBQVEsV0FBVTtBQUFBLFlBQzFCLFdBQVVDLGFBQUEsZ0JBQUFBLFVBQVUsV0FBVTtBQUFBLFVBQ2xDO0FBQUEsUUFDSjtBQUNBLGNBQU0sRUFBRSxRQUFRLFFBQVEsU0FBUyxNQUFJLDJCQUFnQixjQUFjLGFBQWEsTUFBM0MsbUJBQThDLGFBQTlDLG1CQUF3RCxZQUFX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O0FBQy9CLFFBQUMsV0FBbUIsVUFBVSxLQUFLO0FBQUEsTUFDcEMsR0FBRyxHQUFHO0FBQUEsSUFDUCxDQUFDO0FBQUEsRUFDRjtBQUFBLEVBQ0EsbUJBQXlCO0FBQUUsU0FBSyxhQUFhLEtBQUssY0FBYyxZQUFZLFFBQVEsWUFBWSxLQUFLLFNBQVMsc0JBQXNCLENBQUM7QUFBQSxFQUFFO0FBQUEsRUFFdkksSUFBSSxXQUFtQixVQUFVLE9BQWE7QUFBRSxXQUFPLE1BQU0sV0FBVyxPQUFPO0FBQUEsRUFBRTtBQUFBLEVBRWpGLFdBQWlCO0FBQUUsWUFBUSxJQUFJLGVBQWUsS0FBSyxPQUFPO0FBQUEsRUFBRTtBQUFBLEVBRTVELE1BQU0sZUFBOEI7QUFBRSxTQUFLLFdBQVcsT0FBTyxPQUFPLENBQUMsR0FBRyxrQkFBa0IsTUFBTSxLQUFLLFNBQVMsQ0FBQztBQUFBLEVBQUU7QUFBQSxFQUVqSCxNQUFNLGVBQThCO0FBQUUsVUFBTSxLQUFLLFNBQVMsS0FBSyxRQUFRO0FBQUEsRUFBRTtBQUMxRTsiLAogICJuYW1lcyI6IFsiZ2V0RGFpbHlOb3RlU2V0dGluZ3MiLCAiZm9ybWF0IiwgImZvbGRlciIsICJ0ZW1wbGF0ZSIsICJtb21lbnQiLCAiaW1wb3J0X29ic2lkaWFuIiwgImltcG9ydF9vYnNpZGlhbiIsICJpbXBvcnRfb2JzaWRpYW4iLCAiY2hlY2tzdW0iLCAiaW1wb3J0X29ic2lkaWFuIiwgImltcG9ydF9vYnNpZGlhbiIsICJpbXBvcnRfb2JzaWRpYW4iLCAiaW1wb3J0X29ic2lkaWFuIiwgImltcG9ydF9vYnNpZGlhbiIsICJpbXBvcnRfb2JzaWRpYW4iLCAiaW1wb3J0X29ic2lkaWFuIl0KfQo=
