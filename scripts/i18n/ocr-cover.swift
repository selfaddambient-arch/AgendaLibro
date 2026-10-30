// 表紙の画像を Apple Vision で読み、読めた文字を1行ずつ出す（題名の文字化けがないかの機械確認用）。
//   swift scripts/i18n/ocr-cover.swift <画像> <言語コード,…>      例：… cover.png en-US,th-TH
//   swift scripts/i18n/ocr-cover.swift --langs                    Vision が対応している言語の一覧
import Foundation
import Vision
import AppKit

if CommandLine.arguments.count > 1 && CommandLine.arguments[1] == "--langs" {
    let r = VNRecognizeTextRequest(); r.recognitionLevel = .accurate
    print(((try? r.supportedRecognitionLanguages()) ?? []).joined(separator: ","))
    exit(0)
}
let path = CommandLine.arguments[1]
let langs = CommandLine.arguments.count > 2 ? CommandLine.arguments[2].components(separatedBy: ",") : ["en-US"]
guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("ERROR"); exit(1) }
let req = VNRecognizeTextRequest()
req.recognitionLevel = .accurate
req.recognitionLanguages = langs
req.usesLanguageCorrection = false
try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
for o in req.results ?? [] { if let t = o.topCandidates(1).first { print(t.string) } }
