// 画像内の文字を Apple Vision で検出する。検出した文字列を1行ずつ出し、何も無ければ NONE。
//   swift scripts/ocr.swift <画像>...
import Foundation
import Vision
import AppKit

for path in CommandLine.arguments.dropFirst() {
    guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print("\(path): ERROR"); continue }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["ja-JP", "en-US"]
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    let found = (req.results ?? []).compactMap { $0.topCandidates(1).first?.string }.filter { !$0.trimmingCharacters(in: .whitespaces).isEmpty }
    print("\(path.components(separatedBy: "/").last!): " + (found.isEmpty ? "NONE" : found.joined(separator: " | ")))
}
