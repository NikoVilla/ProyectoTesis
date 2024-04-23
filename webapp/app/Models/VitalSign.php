namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\User;
use App\Models\VitalSign;

class VitalSignController extends Controller {
    public function store(Request $request) {
        $user = User::where('unique_id', $request->unique_id)->first();
        if ($user) {
            $vitalSign = new VitalSign($request->all());
            $vitalSign->user_id = $user->id;
            $vitalSign->save();
            return response()->json(['message' => 'Vital signs stored successfully'], 200);
        } else {
            return response()->json(['message' => 'User not found'], 404);
        }
    }

    public function show($unique_id) {
        $user = User::where('unique_id', $unique_id)->first();
        if ($user) {
            $vitalSigns = VitalSign::where('user_id', $user->id)->get();
            return response()->json($vitalSigns, 200);
        } else {
            return response()->json(['message' => 'User not found'], 404);
        }
    }
}
