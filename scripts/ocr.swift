// 画像内の文字を Apple Vision で検出する。「文字」とみなした文字列を出し、無ければ NONE。除外した誤検出も添える。
// 線や模様の誤検出（記号だけ・1文字・確信度が低い）は除き、2文字以上の文字・数字で確信度 0.5 以上のものを「文字」とみなす。
//   swift scripts/ocr.swift <画像>...
import Foundation
import Vision
import AppKit

func isText(_ s: String, _ c: Float) -> Bool {
    let n = s.unicodeScalars.filter { CharacterSet.alphanumerics.contains($0) }.count
    return n >= 2 && c >= 0.5
}

for path in CommandLine.arguments.dropFirst() {
    let name = path.components(separatedBy: "/").last!
    guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        print(name + ": ERROR")
        continue
    }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["ja-JP", "en-US"]
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    var found: [String] = []
    var noise: [String] = []
    for o in req.results ?? [] {
        guard let t = o.topCandidates(1).first else { continue }
        if isText(t.string, t.confidence) {
            found.append(t.string)
        } else {
            noise.append(t.string + "(" + String(format: "%.2f", t.confidence) + ")")
        }
    }
    let head = found.isEmpty ? "NONE" : found.joined(separator: " | ")
    let tail = noise.isEmpty ? "" : "   [除外した誤検出: " + noise.joined(separator: ", ") + "]"
    print(name + ": " + head + tail)
}
