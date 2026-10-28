// 画像内の文字を Apple Vision で読み、行ごとに「文字列」と「1文字ごとの位置（左上原点・割合）」を JSON で出す。黒塗りの位置決め用。
//   swift scripts/ocr-chars.swift <画像>
import Foundation
import Vision
import AppKit

let path = CommandLine.arguments[1]
guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("[]"); exit(0) }
let req = VNRecognizeTextRequest()
req.recognitionLevel = .accurate
req.recognitionLanguages = ["ja-JP", "en-US"]
req.usesLanguageCorrection = false
try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
var out: [[String: Any]] = []
for o in req.results ?? [] {
    guard let t = o.topCandidates(1).first else { continue }
    var boxes: [[Double]] = []
    var idx = t.string.startIndex
    while idx < t.string.endIndex {
        let nxt = t.string.index(after: idx)
        if let b = try? t.boundingBox(for: idx..<nxt) {
            let r = b.boundingBox
            boxes.append([Double(r.minX), Double(1 - r.maxY), Double(r.width), Double(r.height)])
        } else { boxes.append([0, 0, 0, 0]) }
        idx = nxt
    }
    out.append(["text": t.string, "boxes": boxes])
}
let data = try JSONSerialization.data(withJSONObject: out)
print(String(data: data, encoding: .utf8)!)
