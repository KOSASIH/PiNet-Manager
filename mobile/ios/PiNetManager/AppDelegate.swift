import UIKit
import PiNetManagerApi

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    let api = PiNetManagerApi.sharedInstance

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        api.getNodes { nodes, error in
            if let nodes = nodes {
                print("Nodes: \(nodes.count)")
            } else {
                print("Error: \(error?.localizedDescription?? "")")
            }
        }
        return true
    }
}
